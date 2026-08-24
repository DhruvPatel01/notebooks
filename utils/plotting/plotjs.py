import os
import secrets
import textwrap

from IPython.display import HTML


def js_preemble():
    js_path = os.path.dirname(__file__)
    with open(os.path.join(js_path, "./plot.js")) as f:
        plotjs = "<script>\n" + f.read() + "\n</script>"
        plotjs += """
<script>
    window.MathJax = {
    startup: {
      typeset: false  // plotly only (we use katex)
    }
  };
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
<script src="https://cdn.plot.ly/plotly-3.6.0.min.js" charset="utf-8"></script>
"""

    return plotjs        


def random_id(nbytes=4, prefix="id_"):
    return f"{prefix}{secrets.token_hex(nbytes)}"


def indented(txt, indent=4):
    return textwrap.indent(txt, " " * indent)


class Fn:
    def __init__(self, body, x=None, type="line", name=None):
        """Represents 1D Function. Will be called by x argument in JS.
        e.g., Fn("console.log("Hello, World!"); return [1,2,3];").

        Args:
            body: string
            x: custom x (valid js) if this function needs
                otherwise default range will be used
            type: type of this function ('bar' or 'line')
            name: legend to show on plot
        """

        self.body = body.strip()
        self.x = x
        self.type = type
        self.id = random_id(4, "fn_")
        self.name = name

    def __repr__(self):
        return f"""function {self.id} (x) {{ \n{indented(self.body)}\n }}"""

class MapFn(Fn):
    def __init__(self, *args, **kwargs):
        """Example: MapFn('''Math.tanh(x)''') See Fn for more details."""
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"""function {self.id} (x) {{ return x.map(x => {self.body}) }}"""


class HTMLEntity:
    def __init__(self, *args, **kwargs):
        self.id = random_id() + "_" + kwargs.get("name", "")

    def js_get_element_by_id(self):
        id = self.id
        return f"""const {id} = document.getElementById("{id}")"""


class Slider(HTMLEntity):
    def __init__(self, name, min_value, max_value, step, default_value):
        super().__init__(name=name)
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.default_value = default_value
        self.step = step

    def to_html(self):
        return f"""
<div class="plotjs-slider">
    <label for="{self.id}">{self.name}</label>
    <input id="{self.id}" type="range" min="{self.min_value}" max="{self.max_value}" step="{self.step}" value="{self.default_value}"/>
    <otput id="{self.id}_value"></otput>
</div>
""".strip()


class Plot2D:
    def __init__(
        self,
        controls: list[HTMLEntity] | None = None,
        functions: list[str] | None = None,
        x=None,
        limits=(None, None, None, None),
        xlabel="X",
        ylabel="Y",
    ):
        """
        Args:
            x = default x range for the functions
            limits = (xmin, xmax, ymin, ymax)
            xlabel = String to show on xaxis. Can be latex $c$
            ylabel = String to show on yaxis. Can be latex like $mc^2$ or $\\sqrt{(n_\\text{c})}$
        """
        self.html_id = random_id()
        self.controls = controls or []
        self.functions = functions or []
        (xmin, xmax, _, _) = limits
        if not x:
            if (xmin is not None  and xmax is not None):
                self.x = f"linspace({xmin}, {xmax}, 1000)"
            else:
                self.x = "linspace(-2, 2, 1000)"
        else:
            self.x = x
        self.limits = limits

        self.xlabel = xlabel
        self.ylabel = ylabel

        

    def _js_controls(self) -> str:
        return "\n".join(control.js_get_element_by_id() for control in self.controls)

    def _js_outputs(self) -> str:
        return "\n".join()

    def _js_redraw(self) -> str:
        elements = self._js_controls()
        variables = "\n".join(
            f"""const {c.name} = parseFloat({c.id}.value)""" for c in self.controls
        )
        functions_bodies = "\n\n".join(
            [str(fn) for fn in self.functions if isinstance(fn, Fn)]
        )

        data = "["
        for i, fn in enumerate(self.functions):
            name = fn.name or f"trace{i}"
            if isinstance(fn, str):
                assert fn.startswith(("x=>", "x =>")), "Must start with x =>"
                data += f"{{ x, y: x.map({fn}), name: '{name}'}}, "
            elif isinstance(fn, Fn):
                if fn.x:
                    data += f"{{ x: {fn.x}, y: {fn.id}({fn.x}), type: '{fn.type}', name: '{name}' }}, "
                else: 
                    data += f"{{ x, y: {fn.id}(x), type: '{fn.type}', name: '{name}'}}, "
            else:
                raise NotImplementedError(f"Don't know how to convert {fn} into JS")
        data += "]"

        x_min = -10 if self.limits[0] is None else self.limits[0]
        x_max = 10 if self.limits[1] is None else self.limits[1]
        y_min = -3 if self.limits[2] is None else self.limits[2]
        y_max = 3 if self.limits[3] is None else self.limits[3]

        return f"""
function redraw_data() {{
{indented(elements)}
{indented(variables)}
{indented(functions_bodies)}
    const x = {self.x}
    return {data}
}}
function redraw() {{
    const layout = {{
        xaxis: {{
            range: [{x_min}, {x_max}],
            title: {{
                text: "{self.xlabel}"
            }}
        }},
        yaxis: {{
            range: [{y_min}, {y_max}],
            title: {{
                text: "{self.ylabel}"
            }}
        }}

    }}
    Plotly.react('{self.html_id}-plot', redraw_data(), layout)
}}

""".strip()

    def _js_callbacks(self, fn):
        elems = self._js_controls()
        js = "\n".join(
            f'{c.id}.addEventListener("input", {fn})' for c in self.controls
        )
        return f"""
(function() {{
{indented(elems)}
{indented(js)}
    redraw()
}})()
""".strip()

    def render(self, include_plotjs=False, debug=False):
        controls_html = "\n".join(control.to_html() for control in self.controls)
        plotjs = js_preemble() if (debug or include_plotjs) else ""

        redraw_fn = self._js_redraw()
        register_callbacks = self._js_callbacks("redraw")

        # Don't Intend the <div> or <script>. CommonMark breaks.
        s =  f"""
<div id="{self.html_id}">
{indented(controls_html)}
    <div id="{self.html_id}-plot"></div>
{plotjs}
<script type="module">
{indented(redraw_fn, 8)}
{indented(register_callbacks, 8)}
</script>
</div>
"""

        if debug:
            with open("/tmp/plotjs_debug.html", "w") as f:
                print(s, file=f)
                print("Wrote /tmp/plotjs_debug.html")
        return s

    
