# Test Driven Design (TDD)

## Overview

For the context herein, we define *Test Driven Design* (often appreviated as TDD), as a process of converting software requirements into tests that exist prior to the existing code used for computation.  The TDD wiki [page](https://en.wikipedia.org/wiki/Test-driven_development) has a more formal definition, please read if for more context.

## Three Approaches

Consider the ordering of the TDD approach.  Does the approach seem "backward" or "in reverse"?  

Consider other (more common) software development approaches:

* **Just write the code.**  
  * This is the most commonplace approach to software (also considering to be "script writing" and not truly software).
  * That is, a developer goes directly to *implementation*, bypassing the *test* step entirely.
  * In this approach, testing of the code does not exist.
  * The developer never knows if the code works for known solutions and any known edge cases (also known as corner cases and special cases, for example, divide by zero special cases).
  * Worse, the developer cannot modifiy the code and be assured that the updates haven't broken the original code, or introducted new bugs.
  * This philosophy is fast in the short run.  But in the long run, the code suffers because it is untested.  In the attempt to be efficient, the developer has actually been *inefficient* because they have seeded the code base with [technical debt](https://en.wikipedia.org/wiki/Technical_debt), a particularly selfish and shortsighted approach.
* **Write code and then test it.**
  * This approach is slightly better than the aforementioned, because tests exist, which help the development team know code quality, and guard against regressions upon future code updates.
  * But this approach fails to connect the original **requirements** to the software computation.

In contrast with the above approaches, TDD can be considered as

* **Start with the end in mind.**
  * The software requirements are the contract with end users that given an input, a trusted output is computed.
  * Requirements are translated into tests, containing trusted known outputs that the code must pass to be considered pedigreed and trusted.
  * Code is always tested against the code, particularly when/if the original code is updated.

## Requirements

For now, our software has one single requirement:

* **Minimum Scaled Jacobian (MSJ)**:
  * **Given:** A single quadrilateral finite element composed of four nodes (coordinates), where eaach node $p_i$ for $i=1\ldots 4$, has three coordinates $p_i = (x_i, y_i, z_i) \in R^3$, and a connectivity enumerating the four nodes in a right-hand-rule convention.
  * **Find:** A Python function that computes the MSJ.
  * **Reference:** [Quadrilateral Quality](present/quad_quality-2023-07-28.pdf)[^1].

## Tests

To come.

## Computation

To come.

## References

[^1]: See original source `.tex` file at https://github.com/sandialabs/sibl/tree/master/geo/doc/mesh)