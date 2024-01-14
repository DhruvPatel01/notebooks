
## Chapter 1

The book focuses on three important concerns.
1. Reliability: System should continue to work correctly.
2. Scalability: As the system grows, there should be a reasonable way to deal the growth.
3. Maintainability: Over time, different people will work with it. They should be able to work with the system productively. 

### Reliability

Fault: A component of the system deviates from the spec.
Failure: System as a whole stops working.

It is impossible to make number of faults to zero. System should instead be designed so that faults don't cause failures.

#### Hardware Faults
- Mean time to failure of single hardware component is generally large. However, when we have lots of hardware, probability of getting hardware fault increases.

If probability of failure is $\alpha$, and we have N=10_000 components, probability of failing at least one component is $1 - (1-alpha)^N$. 