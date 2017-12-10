## Frequently Asked Questions

#### Why not use GNU's gcc/g++ instead of Intel compilers?

Good question. When I started working on the book around 2010, my initial choice was gcc/g++. I switched to Intel for two main reasons. First, around 2010, the Intel compilers were optimizing loops better. However, I don't believe Intel optimizes loops (such as in dense matrix multiplication or transpose) better than gcc/g++ any more. The new YMM/ZMM registers have raised the difficulty of optimization considerably, and neither compiler does a good job on recent machines with YMM/ZMM registers in 2017.

Second, the advanced computing sites I used, [ARC at Michigan](http://arc.umich.edu/) and [TACC at Texas](https://www.tacc.utexas.edu/), defaulted to Intel compilers. In addition, the Intel compilers make it very easy to link Intel's own Math Kernel Library. The Intel compilers are also free for students.


#### Should I code in assembly?

In 2010, I would have answered no most of the time. However, the situation today is more complicated. Even the best C/C++ compilers don't do a decent job with the new YMM/ZMM registers, and if Intel keeps changing its architectures to  better compete with GPUs, it may be difficult for compilers to catch up. There is a much stronger case for coding in assembly today.


#### I am getting very different timings. Is something wrong?

No. Different timings are to be expected. For example, if you run the Leibniz programs from [here](https://github.com/divakarvi/bk-spca/blob/master/proc/compiler/leibniz.cpp), you will get different numbers. The only way to resolve this matter is to look at the instruction stream generated, a point that is emphasized in the [discussion](https://divakarvi.github.io/bk-spca/spca.html#toc-Subsection-3.2.2).

In the [discussion](https://divakarvi.github.io/bk-spca/spca.html#toc-Subsection-3.2.5) of matrix multiplication, it is noted that the same Intel compiler does a much better job on the older SSE2 than the newer AVX2 for multIJKX(). Compilers can be quite unpredictable, and that will not change.

