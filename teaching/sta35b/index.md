STA 035B, Winter 2024
=======================

**Instructor**: Spencer Frei (sfrei@ucdavis.edu)

**Lectures**: Mondays, Wednesdays and Fridays, 4:10 PM - 5:00 PM, WELLMN 234

**Labs**: Run by TA, Mengjie Shi, email: mjshi@ucdavis.edu

* Section A01: Tuesdays, 10:00 AM - 10:50 AM, TLC 2212

* Section A02: Tuesdays, 11:00 AM - 11:50 AM, TLC 2212

**Final exam**: Friday March 22 at 8:00 AM 


**Office hours**:
* Spencer Frei: Wednesdays, 2:30 PM - 3:30 PM, MSB 4220
* Mengjie Shi: Tuesdays, 2:00 PM - 4:00 PM, Academic Surge 2142


**Syllabus**: [here](syllabus.html)

**Piazza**: [here](https://piazza.com/ucdavis/winter2024/sta035ba01wq2024)

**Textbooks**: 
There will be two textbooks used for the course, both of which are freely available online.  

* Mine Cetinkaya-Rundel, Johanna Hardin.  Introduction to Modern Statistics [IMS].  [link](https://leanpub.com/imstat)
* Hadley Wickham, Mine Cetinkaya-Rundel, Garrett Grolemund. R for Data Science, 2nd edition [R4DS2]. [link](https://r4ds.hadley.nz/)


# Class Schedule


Lecture Day | Topics | Slides | Additional references  | HW | Lab | Notes
--- | --- | --- | --- | --- | --- | --- 
Jan 8 (M) | Intro, review of R / dplyr | [Slides](http://spencerfrei.github.io/teaching/sta35b/lectures/lec01-dplyr/lec01-dplyr.html#1) | R4DS2 Ch3 |  
Jan 10 (W) | dplyr, tidy data | [Slides](http://spencerfrei.github.io/teaching/sta35b/lectures/lec02-dplyr-2/lec02-dplyr.html#) | R4DS2 Ch3 | 
Jan 12 (F) | Tidy data and transformations of logical vectors | [Slides](http://spencerfrei.github.io/teaching/sta35b/lectures/lec03-transformation-logical-vectors/lec03-transformations-logical-vectors.html)|  R4DS2 Ch5 and Ch12 | No HW | 
Jan 15 (M) | **MLK Day, no class** | | | | [Lab 1 released](http://spencerfrei.github.io/teaching/sta35b/labs/lab1.Rmd)
Jan 17 (W) | Transformations of numbers | [Slides](http://spencerfrei.github.io/teaching/sta35b/lectures/lec04-transformations-numbers/lec04-transformations-numbers.html) |  R4DS2 Ch13 | | 
Jan 19 (F) | Transformations of strings | [Slides](http://spencerfrei.github.io/teaching/sta35b/lectures/lec05-transformations-strings/lec05-transformations-strings.html) | R4DS2 Ch14 |  HW 1 released [[Rmd]](http://spencerfrei.github.io/teaching/sta35b/hw/hw1.Rmd) [[PDF]](http://spencerfrei.github.io/teaching/sta35b/hw/hw1.pdf) [[Solution]](http://spencerfrei.github.io/teaching/sta35b/hw/hw1_sol.pdf)
Jan 22 (M) | Regular expressions | [Slides](http://spencerfrei.github.io/teaching/sta35b/lectures/lec06-transformations-regular-expressions/lec06-ioslides_transformations-regular-expressions.html) | R4DS2 Ch15 | | **Lab 1 due, 9pm** <br> [Lab 2 released](http://spencerfrei.github.io/teaching/sta35b/labs/lab2.Rmd)
Jan 24 (W) | Dates and Times | [Slides](http://spencerfrei.github.io/teaching/sta35b/lectures/lec07-dates-and-times/lec07-dates-and-times.html) | R4DS2 Ch17 | **HW 1 due 1/25, 9pm**
Jan 26 (F) | Joins, Visualization 1 | [Slides 1](http://spencerfrei.github.io/teaching/sta35b/lectures/lec08-joins/lec08-joins.html) [Slides 2](http://spencerfrei.github.io/teaching/sta35b/lectures/lec09-visualization-1/lec09-visualization-1.html)| R4DS2 Ch19  / Ch9| HW 2 released  [[Rmd]](http://spencerfrei.github.io/teaching/sta35b/hw/hw2.Rmd) [[PDF]](http://spencerfrei.github.io/teaching/sta35b/hw/hw2.pdf) [[Solution]](http://spencerfrei.github.io/teaching/sta35b/hw/hw2_sol.pdf)
Jan 29 (M) | Visualization 2 | [Slides](http://spencerfrei.github.io/teaching/sta35b/lectures/lec10-visualization-2/lec10-visualization-2.html) |  R4DS2 Ch9 | [Practice midterm](http://spencerfrei.github.io/teaching/sta35b/exams/midterm_practice.pdf) | **Lab 2 due, 9pm** <br> [Lab 3 released](http://spencerfrei.github.io/teaching/sta35b/labs/lab3.Rmd)
Jan 31 (W) | Visualization 3 | [Slides](https://spencerfrei.github.io/teaching/sta35b/lectures/lec11-visualization-3/lec11-visualization-3.html) | R4DS2 Ch10 | **HW 2 due 2/1, 9pm** 
Feb 2 (F) | Visualization 4 | [Slides](https://spencerfrei.github.io/teaching/sta35b/lectures/lec12-visualization-4/lec12-visualization-4.html) | R4DS2 Ch11 & 16 | 
Feb 5 (M) | **Midterm 1** | | | | **Lab 3 due, 9pm** <br> [Lab 4 released](http://spencerfrei.github.io/teaching/sta35b/labs/lab4.Rmd)
Feb 7 (W) | Functions 1 | [Slides](https://spencerfrei.github.io/teaching/sta35b/lectures/lec13-functions-1/lec13-functions-1.html) | R4DS2 Ch25 | | 
Feb 9 (F) | Functions 2 / Linear regression | [Slides](https://spencerfrei.github.io/teaching/sta35b/lectures/lec14-functions-2/lec14-functions-2_v0.html) | R4DS2 Ch25 | HW 3 released  [[Rmd]](http://spencerfrei.github.io/teaching/sta35b/hw/hw3.Rmd) [[PDF]](http://spencerfrei.github.io/teaching/sta35b/hw/hw3.pdf) [[Solution]](http://spencerfrei.github.io/teaching/sta35b/hw/hw3_sol.pdf) 
Feb 12 (M) | Linear regression | [Slides](https://spencerfrei.github.io/teaching/sta35b/lectures/lec15-linear-regression-2/lec15-linear-regression-2.html) | IMS Ch7-8, Ch10 | |**Lab 4 due, 9pm** <br> [Lab 5 released](http://spencerfrei.github.io/teaching/sta35b/labs/lab5.Rmd)
Feb 14 (W) | Inference - randomization | [Slides](https://spencerfrei.github.io/teaching/sta35b/lectures/lec16-inference-1/lec16-inference-1.html) | IMS Ch11 | **HW 3 due 2/15, 9pm**
Feb 16 (F) | Inference - bootstrapping, mathematical models| [Slides](https://spencerfrei.github.io/teaching/sta35b/lectures/lec17-inference-2/lec17-inference-2.html) | IMS Ch12-13 | HW 4 released [[Rmd]](http://spencerfrei.github.io/teaching/sta35b/hw/hw4.Rmd) [[PDF]](http://spencerfrei.github.io/teaching/sta35b/hw/hw4.pdf) 
Feb 19 (M) | **Presidents' Day, no class** | | |  | [Lab 6 released](http://spencerfrei.github.io/teaching/sta35b/labs/lab6.Rmd)
Feb 21 (W) | Inference for proportions | [Slides](https://spencerfrei.github.io/teaching/sta35b/lectures/lec18-inference-3/lec18-inference-3.html) | IMS Ch15-16 |  | **Lab 5 due, 9pm** <br>
Feb 23 (F) | Inference for comparing 2 proportions|  [Slides](https://spencerfrei.github.io/teaching/sta35b/lectures/lec19-inference-two-proportions/lec19-inference-two-proportions.html) | IMS Ch17 | **HW 4 due 2/23, 9pm**| 
Feb 26 (M) | No class |  |  | | **Lab 6 due, 9pm** 
Feb 28 (W) | **Midterm 2** | | | 
Mar 1 (F) | Inference for comparing 2+ means | Slides | IMS Ch19-20, 22 |  HW 5 released
Mar 4 (M) | Inference for comparing 2+ means | Slides | IMS Ch19-20, 22 | | Lab 7 released
Mar 6 (W) | Inference for comparing 2+ means | Slides | IMS Ch19-20, 22 | **HW 5 due 3/7, 9pm**
Mar 8 (F) | Inference for regression | Slides | IMS Ch24
Mar 11 (M) | Inference for regression | Slides | IMS Ch24-25 | | **Lab 7 due, 9pm**
Mar 13 (W) | Inference for regression | Slides | IMS Ch25 
Mar 15 (F) | Review 


