## Corrections and Improvements

* pages xii, xix, 82, 584, 585, 586: in github.com/divakarvi/Book-SPCA, replace Book-SPCA by bk-spca, although both web addresses work.


* page xix:  "In fact the interpreted languages can be several hundred times [slower]."

* page xx: "In addition to showing me how to get started with Linux" --> "In addition to helping me overcome the hurdle of building and loading Linux"

* page 47: "Objected oriented programming can be done in plain C as well as using pointers." --> replace "as well as" by "as well."

* page 65: "This convention is common among Fortran compilers but not universal." --> omit "but not universal."

* page 74: "BLAS and LAPACK functions[, to which we now turn,] typically have long argument lists."

* page 118: "Unlike the Vector and Matrix classes from before" --> "Unlike the Vector class from before."

* page 131: "lu decomposition" --> "LU decomposition."

* page 237: "time to issuing a load/store instruction that triggers a DRAM access and its complection" --> replace "to" with "between."

* page 272: "The measurements in the first two rows are not valid." ---> omit, sentence should not be here.

* page 319: "The Pthread library will access administrative information about the threads using these variables." --> "At a minimum, the administrative information will include the process id for each thread. The process id is used by the library to make Linux system calls for initiating, managing, and terminating the thread."

* page 319: "C/C++ compilers [include] Pthread header files by themselves without any prompting."

* page 320: "Thread stacks" ---> Say a little more about mutexes, and spinlocks. Why there are in global memory and not on thread stacks.

* page 321: "On the first line, a variable mutex is defined and initialized." --> Explain why it is global, the kind of administrative information it may hold. Think of a mutex as a location in memory as a first and useful approximation.

* page 331: "are complete before any loads and stores after it occur." -->  "are complete before any loads and stores after it are issued." 

* page 505: In Figure 5.3, "2x32 Mem Ch" should be lifted a few mm.

* page 538: "Inside a streaming multiprocessor is different from a processor core." --> "Internally, a streaming multiprocessor is different from a processor core."

* page 564: "The nvcc compiler driver offers options for generating .ptx files with only the PTX or .cubin files with only the elf binary or even .o files with the elf binary for multiple compute capabilities as well as PTX." --> "With suitable options, the nvcc compiler driver will generate .ptx files with only PTX or .cubin files with only the elf binary. It can also generate .o files with  elf binaries for multiple compute capabilities in addition to PTX."

* page 584: "Python or Matlab" --> Python.
