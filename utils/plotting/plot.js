function linspace(start, stop, num=100) {
    const step = (stop - start)/(num-1);
    return Array.from({length: num}, (_, i) => start + i*step);
};