STA 250 - Theoretical Foundations of Modern AI, Winter 2024
==============

Instructor: Spencer Frei 

Time: 12:10pm-1:50pm Mondays and Wednesdays

Location: Storer 1342

Office hours: 2:30pm-3:30pm Fridays, MSB 4220

## Information

This course serves as a survey of topics on the mathematical and statistical foundations of deep learning, the technology that underlies modern artificial intelligence.   Topics covered include:

* Function approximation with neural networks
* Convex and non-convex optimization
* Implicit regularization of optimization algorithms
* Uniform convergence and benign overfitting
* Adversarial examples and adversarial robustness
* Transformers and large language models

The course will be primarily proof-based but will also involve programming in Python (PyTorch/Jax/TensorFlow).  Prerequisites include familiarity with programming in Python, basic machine learning, proof-based linear algebra, and probability theory.  The course is ideally suited for motivated PhD students in Statistics, Mathematics, and Computer Science.  It will be a fairly intensive course.


## Course structure and evaluation

The first ~8 weeks of the course will consist of lectures, in-class quizzes, homeworks, and in-class reading group discussions.  The last ~2 weeks of the course will be for presenting final projects.

* Homework: 25%. 2 homeworks, 12.5% each.
* In-class quizzes: 10%. 6 short in-class quizzes, with worst two scores dropped (2.5% each). 
* Reading group discussions: 30%.  (Details below.) 
* Project: 35%.  (Details below.)

A more detailed week-by-week schedule can be found at the bottom of this page.  

## Homework
Before the course begins, students should complete the attached [Homework 0](sta250-homework0.pdf); this will not be collected, and no solutions will be provided, but should serve as a self-assessment.   If you struggle with completing any of the non-programming questions, then the course will likely be quite difficult without a significant investment on your part. 

If you are unfamiliar with software packages like PyTorch/Jax/TensorFlow, I would recommend getting started with PyTorch with the following tutorials.  
* [PyTorch: Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html) 
* [Introduction to PyTorch - YouTube Series](https://pytorch.org/tutorials/beginner/introyt.html)

All of the coding you will need to do for the course (and tutorial) can be done on your own laptop or on [Google Colaboratory](https://colab.research.google.com/?utm_source=scs-index) - a GPU will not be needed, although using the Google Colab GPU may help if you want to do an experiment-focused project. 

You are welcome to collaborate with other students on your homework, but you must acknowledge this by writing the names of those with whom you collaborated at the top of your homework assignment.  All homeworks must be written individually.  You must submit your homeworks as LaTeX'd PDFs on Gradescope (accessible via Canvas).  

Each homework will be graded on a random subset of the problems assigned.  Homeworks will be graded for clarity of writing in addition to correctness. 

## In-class quizzes
There will be 6 short in-class quizzes.  The worst two quizzes will be dropped, and the remaining 4 quizzes will constitute 10% of the grade.  The quizzes will be open book (but no internet).   It is highly recommended that you are consistently reviewing the material after it is presented in the lecture. 

## Reading group discussions
Throughout the course, we will spend 3 or 4 sessions thoroughly reading and discussing an influential paper related to the course material.  The format for these discussions will be structured along the lines of [Colin Raffel and Alec Jacobson's role-playing student seminars](https://www.cs.toronto.edu/~jacobson/images/role-playing-paper-reading-seminars.pdf), also used by [Aditi Raghunathan](https://www.cs.cmu.edu/~aditirag/teaching/15-884F22.html).  For more details on the reading group, please see [this page](reading_group.html). 

## Project
There will be a final project for the course.  For more details, see [this page](project.html).



## Class Schedule
References:

[T] - Telgarsky, deep learning theory 2021-10-27 v0.0-e7150f2d [pdf](https://mjt.cs.illinois.edu/dlt/index.pdf)

[SSBD] - Shalev Shwartz and Ben-David, Understanding Machine Learning

[AEP1] - Andréasson, Evgrafov, & Patriksson - [An Introduction to Continuous Optimization
Foundations and Fundamental Algorithms, 1st ed](https://www.google.com/books/edition/An_Introduction_to_Continuous_Optimizati/dxdCHAAACAAJ?hl=en)


Lecture Day | Topics | Lecture notes | Additional references  | HW/Project/Reading Group | Other 
--- | --- | --- | --- | --- | --- 
Jan 8 (M) | Overview, approximation theory | [PDF](http://spencerfrei.github.io/teaching/foundations/notes/lec01-intro-approximation_annotated.pdf) | [T] Ch2|  
Jan 10 (W) | Convex optimization | [PDF](http://spencerfrei.github.io/teaching/foundations/notes/lec02-convex-opt_annotated.pdf) | [T] Ch7 | Paper discussion groups assigned
Jan 15 (M) | **MLK Day, no class** | | |  
Jan 17 (W) | Non-convex optimization | [PDF](http://spencerfrei.github.io/teaching/foundations/notes/lec03-non-convex-opt_annotated.pdf) | [Karimi et al '16](https://arxiv.org/abs/1608.04636) | HW 1 released [[PDF]](http://spencerfrei.github.io/teaching/foundations/hw/hw1.pdf)  <br> 
Jan 22 (M) | Constrained optimization<br> KKT conditions | [PDF](http://spencerfrei.github.io/teaching/foundations/notes/lec04-constrained-opt_annotated.pdf) | [AEP1] Ch5,<br> [Lyu-Li'19](https://arxiv.org/abs/1906.05890) | **Paper discussion report<br> due 1/23, noon**
Jan 24 (W) | **Paper discussion: <br> [Edge of Stability](https://arxiv.org/abs/2103.00065)** | |
Jan 29 (M) | Implicit regularization I | [PDF](http://spencerfrei.github.io/teaching/foundations/notes/lec05-implicit-reg_annotated.pdf) | [T] Ch10 | 
Jan 31 (W) | Implicit regularization II |  [PDF](http://spencerfrei.github.io/teaching/foundations/notes/lec05-implicit-reg_annotated.pdf) | [T] Ch10 | **Project milestone #1 due**
Feb 5 (M) | Uniform convergence I | [PDF](http://spencerfrei.github.io/teaching/foundations/notes/lec06-generalization_annotated.pdf)| [SSBD] Ch 26;<br> [T] Ch13| 
Feb 7 (W) | Uniform convergence II | [PDF](http://spencerfrei.github.io/teaching/foundations/notes/lec06-generalization_annotated.pdf)|  [SSBD] Ch 26; <br> [T] Ch13 <br> [McDiarmid Ineq. proof](https://www.cs.columbia.edu/~djhsu/coms4995-s20/lectures/mcdiarmid-notes.pdf)| 
Feb 12 (M) | Uniform convergence III; <br> Benign overfitting I| PDF | | **Project milestone #2 due**;<br> **Paper discussion report due 2/13, noon**
Feb 14 (W) | **Paper discussion:<br> [Understanding DL requires<br> rethinking generalization](https://arxiv.org/abs/1611.03530)** |  | | **HW 1 due**
Feb 19 (M) | **Presidents' Day, no class**
Feb 21 (W) | Benign overfitting II | PDF | | HW2 released; <br>**Paper discussion report due 2/25, noon**
Feb 26 (M) |  **Paper discussion:<br> [Adversarial examples:<br>Bugs or features?](https://arxiv.org/abs/1905.02175)**
Feb 28 (W) | Transformers I   | PDF
Mar 4 (M) | Transformers II | PDF | | **Paper discussion report due 3/5, noon**
Mar 6 (W) | **Paper discussion:<br> [In-context learning](https://arxiv.org/abs/2208.01066)**
Mar 11 (M) | Final projects I | | | 
Mar 13 (W) | Final projects II | | | **Project reports due @ noon**; <br>**HW 2 due**


## Related courses
This course is inspired by a number of other courses, including:

Quanquan Gu, UCLA - [Foundations of Deep Learning](https://uclaml.github.io/CS269-Spring2022/)

Tengyu Ma, Stanford - [Machine Learning Theory](https://web.stanford.edu/class/stats214/)

Aditi Raghunathan, CMU  - [Theoretical and Empirical Foundations of Modern Machine Learning](https://www.cs.cmu.edu/~aditirag/teaching/15-884F22.html)

Matus Telgarsky, NYU - [Deep Learning Theory](https://mjt.cs.illinois.edu/courses/dlt-f22/)

Fanny Yang, ETH Zurich - [Guarantees in Machine Learning](https://sml.inf.ethz.ch/gml23/syllabus.html)





