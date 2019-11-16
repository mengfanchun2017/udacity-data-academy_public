# # DSND Capestone Project (Sparkify): Want to quit? I got U!

[TOC]

# What is this post about?
## / start from an udacity project requirment
Hi everyone, I am a Udacity `Data Scientist Nanodegre` student, my name is Francis and I am come from China.

In this task, I am going to write a data science blog that can talk about some finding on data and illustrate how a data science can do.

I take the recommended data `stack overflow survey` and I want to give a meaningful introduction or explor for myself on how data science work in daily life. 

## / data science working framework
My data science analysis framework is from `Udacity Data Sciencest Nanodegree`, here is a brief introduction, you can find it out at www.udacity.com or google if you want to learn more.

Data Science CRISP-DM (Cross Industry Process for Data Mining) Frame Work: 
1. Business Understanding
2. Data Understanding
3. Prepare Data
4. Data Modeling
5. Evaluate the Results
6. Deploy

## / my experience with sparkify

As I am lived in China, I do not use sparkify. It is heard that sparkify is founded after the founder was reject by google. And when google want to take sparkify, he gave a very high price to show his attitude: NO WAY!

In China I subscribed Netease Musicdata before, and now take Xiami music vip account. 

From my point of view, online music company is much more rely on technology. For there are huge songs in the world, and the recommendation and service is more useful to a user, if it really goes into ones heart. (As contrary to online vedio company).

## / content list
According to this Project Requement, I first make some mess to my reviewer. I found that there maybe one thing tricky: althrough I choose my git reop at submit page, but my reviewer seems get all the file rather than the reop links.

So I put the two requirement links below here for clear:
- repo links(github):
- blog links(medium):

And for the file in the repo, a short explain is here:
--- code file (ipynb for run, html for read) ---
1 Sparkify_lm_3.ipynb
2 Sparkify_lm_3.html
--- post file (medium for this post, README for introduction) ---
3 README.pdf
4 README.md
5 medium_ori.md
--- data file ---
6 mini_sparkify_event_data.json.bz2

You can run the .ipynb file at your env (or just take a look at .html file). And you need the data file for I compressed it to save storage. (or you can change the code a bit). 

# How I found about the data?
The full dataset is 12GB, of which you can analyze a mini subset in the workspace on the following page. Optionally, you can choose to follow the instructions in the Extracurricular course to deploy a Spark cluster on the cloud using AWS or IBM Cloud to analyze a larger amount of data. Currently we have the full 12GB dataset available to you if you use AWS. If you use IBM, you can download a medium sized dataset to upload to your cluster.

Details on how to do this using AWS or IBM Cloud are included in the last lesson of the Extracurricular Spark Course content linked above. Note that this part is optional, and you will not receive credits to fund your deployment. You can do the IBM portion for free. Using AWS will cost you around $30 if you run a cluster up for a week with the settings we provide.

Once you've built your model, either in the classroom workspace or in the cloud with AWS or IBM, download your notebook and complete the remaining components of your Data Scientist Capstone project, including thorough documentation in a README file in your Github repository, as well as a web app or blog post explaining the technical details of your project. Be sure to review the [Project Rubric](https://review.udacity.com/#!/rubrics/2345/view) thoroughly before submitting your project.


# My Workout (detailed at jupyter notebook file)

## / work structure
![-c](media/15705180791749/15727447092738.jpg)

## / request for coaching
As taking the work out I come up with these 2 questions:
- **Q1:How to practice Sprak at real world?** I am new to spark, I manage about 3 week to finish this project, and still get some unclear on part of it. So where can I get some real big data to explore the skill of spark (on AWS, not local). Can you share something?
- **Q2:Spark vs Flink** I do some research that both Spark and Flink are super-stars nowadays. While Spark come from batch to stream, and Flink come from stream to batch. How shoud I choose from them. Or for the short, what are the pro and cons for Spark and Flink on differed situation?

## / version 
- version1 - start trying workout.
- version2 - finish uda workplace run out.
- version3 - finish local run out. (mac env)
- version4 - (finished at next submit) - aws emr run out, and take a new chaper at the end `/Plus/ AWS EMR note`

## / feelings
For this project, I review many data analys skill and get some new try. Some are good, and some are failure. I am afrid I do not have time to complete all I thought at the begining.

But this is still a good start, maybe after my graduation from Udacity Data Scienst Nanodegree, I will write and publish more offten.

# My findings
For the ease of read on this post, please refer to my git for notebook file if you are interested. Here is only what I found out with project.

## / conclutions
As taking three methord (lr, dt, gbt) to compute the prediction, it turned out that lr get the best score (nearly 0.65).

So is it the best? My answer is: No!

For mathine learning is a tech that take the data into result. For the workplace and Local, I used only 128MB data to train, but the real data is 12GB (only use 1%).

So when this case is being run at real world(althrough very simple), the amount of data shoud take great consideration.

## / learnings
As an spark newbie, I got many time on local env preparation. For there are some tricky points that I have to workout to proceed (take 3 example):
- Java8 is required: and it really matters (my mac have Java12... and it really not works... ooops)
- Bear in mind Lazy Cauculation: so some code is run at the point it requier output, and it will run all needed code cell above (compare to pandas, I always thought there is something wrong)
- Some times you do not need to do everything: AWS EMR get your work for Saprk very handy. You do not have to do every thing for a very small fee(remember to shut down your vm, and use SPOT)

## / Future 
I am plannign to try out full data (12GB) at AWS EMR, which is a more real story on business.
