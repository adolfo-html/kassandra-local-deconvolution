# Training and applying BostonGene's Kassandra deconvolution model on a public ccRCC RNA-seq sample 

## Introduction

Hi! This is a machine learning project I'm doing aimed at studying how the Kassandra ML algorithm is used to help oncology research.



(1/20)

### Personal Log

Sooo I need a job. I've been cold calling a lot of software, data, tech, and IT companies (a surprising amount of companies I've reached out to have bad phone support). I've got actual skills and experience in software development and computer science, I've made real apps, I've gotten awards and recognition (ask me about my capstone project, I got 1st place at the expo), and now I have my bachelor's degree.

I've also made a few networking connections! Here in Houston, there are several healthcare organizations that I'd love to work for. It's important, good work, and my resume will look amazing from it.

There's one group in particular that has sparked my interest in oncology research - BostonGene. They're a rising oncology research company that contributes to cancer research and treatment! They've partnered with companies like AstraZeneca and Johnson & Johnson to advance therapies and medication.

Since I'm doing a big important project like this, I also wanted to document the whole thing on GitHub in my personal style - **EASY TO UNDERSTAND!!!** So that anyone who's just as curious can learn easily and we can all save the world one day.

But like... what am I gonna do??

I was reading about BostonGene and studied some of their publications. I was really interested in the AI/ML part of their work, because I took courses over those and have experience making applications with them, so maybe I could contribute with that. BostonGene developed a machine learning algorithm named Kassandra that they used to research tumor microenvironments! And it's available on GitHub!!!

At first I was like "Maybe I could try recreating the project by training Kassandra myself using some publicly available datasets!" because those are two big things people like seeing - experience with handling big data, and doing cool machine learning stuff. But training ML models requires computing resources I don't have. I just have a laptop. It's a newer Lenovo and I love it, but I would need a supercomputer.

> Note: I would later find out that you do not need a supercomputer to train a Kassandra model locally.

I think what I should do is just use Kassandra. I can try to find some publicly available datasets of bulk RNA-seq data from tumor samples, and then use Kassandra to analyze them and see what insights I can get about the tumor microenvironments. That way, I can show that I know how to use ML tools in a real-world context, and also contribute to cancer research in some small way.

## The Project Right Now


(1/21)

### Kassandra

From the BostonGene [website](https://science.bostongene.com/kassandra):

"Here, we present Kassandra, a robust and accurate cell deconvolution tool developed for analysis of healthy tissue and tumor biopsies. Based on RNA-seq NGS data of a biological sample, Kassandra predicts cellular composition including stromal and immune elements by analyzing the gene expression. This will lead to an improved understanding of the tumor microenvironment, which is a critical factor in cancer pathogenesis, clinical outcome, and therapeutic resistance.

Kassandra is a decision tree machine learning-algorithm trained on a collection of over thousands of RNA profiles from various sorted cell types. Performance was validated on over 4,000 H&E tissue slides and more than 1,000 samples comprising normal and tumor tissues by comparison with cytometric, immunohistochemical or single-cell RNA sequencing measurements of the same tissue."

So! Kassandra **deconvolves** the RNA-seq data. Its goal is to take the tumor sample and **predict its cellular composition** - meaning predict what types of cells are in the tumor, and how many of each type there are. 

To give you an example of how this is useful, BostonGene published a study - "Tumor-associated macrophage (TAMs) and cancer-associated fibroblasts (CAFs) profiles in invasive lobular carcinoma (ILC) vs no special type (NST)" - where they used Kassandra to analyze the microenvironment of breast cancer tumor samples. They aimed to compare the microenvironment composition of ILC vs NST breast cancer subtypes. They plugged the bulk RNA-seq data into the Kassandra algorithm, which showed that there's not much difference in the compositions of the tumors. They're both really resistant to the immune system. But, it pointed BostonGene towards a more probable place where the resistance is coming from.

And here's a simpler explanation of Kassandra's process: A tumor sample is taken from a patient, and we extract RNA sequence data from it. So one data file is basically a big list of snippets from all the RNA strands of every cell in a tumor sample. 

Lemme repeat that: At first, the data we get is a big list. It's a bunch of PARTS of RNA strands. There are a LOT of parts, and they are all jumbled up together. That's what we have! Cracked RNA strands.

But yeah, remember that all these parts are from ALL the cells in the tumor sample.

Then that data becomes a gene-expression vector that has the number of times each gene is spotted in the sample, which is where Kassandra comes in to calculate the cell type proportions. From this, Kassandra predicts the cellular composition of a tumor sample and the proportions of each cell type in it.

Awesome! I understand it a lot better now - I guess enough to continue to actually doing the project. So what I'm going to do is download the baby Kassandra ML algorithm (the GitHub has a small version that can run on the average laptop), and then plug in an RNA seq file so it can give me an output. I actually just found [this site](https://science.bostongene.com/kassandra/downloads) that has relevant files from BostonGene's study.

Turns out the page also has a 'Tool' tab where I can actually use the Kassandra algorithm online! Just needs your email. Unfortunately, *right now, this service is down for maintenance*. Of course.

### Some Quick Explanations

*Transcripts*: So we have genes in DNA/RNA. Each gene can come in different versions! Each version is a transcript.

*TPM*: "Transcripts per million". A normalization method. So when we say "TPM gene expression matrix", it means a table that shows how much each transcript is expressed in the sample, and it's a little cleaner and has less redundant data now. 

Another important thing to note. Kassandra is designed to predict the cellular composition of a tumor sample (or blood sample, because I think the researchers actually made two models of Kassandra in the study, one for blood and one for tumors). But I was wondering if Kassandra was trained to work with only one TYPE of tumor. But here's an important line from the study:

"A collection of more than 18,000 bulk RNA-seq, covering numerous immune and stromal sorted cell populations and cancer cell lines, was curated using the GEO and ArrayExpress databases (Barrett et al., 2012). The raw RNA-seq datasets were combined, homogeneously annotated, and bioinformatically recalculated for comparable measurements of transcript expression within each cell type to reduce batch effects. After quality control, well-defined cell clusters were revealed, populating the Kassandra sorted cell compendium with purified RNA-seq samples (n = 9,404) of diverse immune and stromal cell populations, including malignant cells from 24 cancer types (n = 2,166) (Figures 1B, S2A, and S2B)." (Zaitsev et al., 2022)

Look at me, citing my sources. So it looks like Kassandra can work with multiple cancer/tumor types! I'm hoping the data that I find to plug into Kassandra will be compatible in this way.


(1/22)

### What I'm Gonna Do To Get Results

Right now I've got a basic idea of how to get from Kassandra to results that doctors and researchers use. Here's the game plan:

Download Kassandra -> Find a bulk RNA-seq dataset from a tumor sample (fastq file) -> Plug that data into **Kallisto** -> Get a TPM gene expression matrix -> Plug that into Kassandra -> Get the predicted cellular composition -> Analyze and explain the results

**Kallisto** is the middle ground between the raw RNA-seq data and the data Kassandra needs. It takes the fastq files with the cracked RNA strands, calculates which transcript (isoform) each RNA strand belongs to, and estimates how much each transcript is being expressed. So its output is a TPM transcript expression matrix! Idk what file type that is though. Guess I gotta use it

Anyway, then THAT data can go into Kassandra. So I'm pretty sure how this is gonna go is... Start with the file of RNA-seq data, then somehow get access to Kallisto. Then configure Kallisto, then input the data, then get the output matrix file, then plug that into Kassandra, then MONEY.

I found the full study [here](https://www.sciencedirect.com/science/article/pii/S1535610822003191). Hadn't seen the full version before. It turns out they do a lot more than just plugging in the data into a couple algorithms to get the final product. They do a lot of work like training the model with simulated / realistically noisy data, validating the results with histology, and intense explaining why the results are reliable. But I won't focus on that - I'm just trying to learn how to get the useful stuff.

To summarize an important thing about their study: They got 18000 raw, messy samples first, to do the first normalization and artificial transcriptome generation specifically to train the model. They had to process the data a little bit, though, because they wanted to add noise so the model was more accurate to real tumors. Then they got another raw RNA-seq data file (like I'm gonna do) and simply plugged it in to get the results.

Just to recap... I'm trying to get from a raw tumor sample to the valuable knowledge that Kassandra generates. So I'll start with getting the RNA-seq data!


(1/23)

### How Anyone Can Get RNA-Seq Data

First of all, let's research how BostonGene got and used their RNA-seq data.

Basically, they got a bunch of data from the GEO and ArrayExpress databases, then they used those in the *training Kassandra* part. So I guess I could use those databases to get RNA-seq data too? Maybe I should get my sample from a different database?

At first, I tried the NIH National Cancer Institute's Genomic Data Commons (GDC) Portal. I searched for anything with "fastq", turned the "open" access filter on, and tried the "RNA-seq" experimental strategy. But there weren't any BAM files (files that can be turned into fastq files with a tool) or fastq files, so I guess I gotta look elsewhere.


(1/25)

After looking around some more, I found the NCBI's Sequence Read Archive (SRA) database. This one looks like it's got what I need!

The thing is, the data I need to plug in to Kallisto obviously needs to be a very specific type of data.
- It needs to be a fastq file, which means it's raw RNA-seq data
- It needs to come from a tumor sample 
- It needs to be a HUMAN sample, because it turns out SRA has a lot of animal data too
- It needs to be RNA-seq experimental strategy, to guarantee that it's transcriptomic data that comes from RNA sequencing
- It needs to be open access (duh)

There are a few different results that I looked at. I'll go through how I narrowed down my search to get the best possible data for Kassandra by showing the results I got from my searches:



*ERX14406805: Illumina NovaSeq 6000 paired end sequencing*

This is when I used "(fastq) AND "Homo sapiens"[orgn]" as my filter. I'm not sure if the 'fastq' filter worked, but it certainly got me more sequencing results. So I was just looking for fastq files here.

This was part of a study called "Tracing Clonal Hematopoiesis and Lymphoma-Associated Mutations in Hematopoietic Progenitors in B-Cell Non-Hodgkin Lymphoma". The sample name was called "NHL27_Tumor". So I thought cool, I found a lymphoma sample! But, in the "Library" details, it had a few properties that looked off:

>Name: NHL27_Tumor

>Instrument: Illumina NovaSeq 6000

>Strategy: WXS <- *Isn't this supposed to be RNA-seq*

>Source: GENOMIC <- *Why are we looking at the genome*

>Selection: other <- *What is this*

>Layout: PAIRED <- *What is this*

Here's a good explanation I made with ChatGPT's help:

"The strategy was wrong. WXS (Whole Exome Sequencing) measures DNA, not RNA, and is used to detect mutations in coding regions rather than gene expression. The GENOMIC source confirms that the data comes from DNA instead of transcripts.

Kassandra requires transcriptomic data because cell identity is encoded in gene expression patterns, not in the static genome. Transcriptomic (RNA-seq) data shows which genes are active and how strongly they are expressed in the tumor sample. Kallisto uses this RNA-seq signal to estimate transcript abundances (TPM), which Kassandra then uses to infer the proportions of different cell types in the tumor microenvironment."

So that wasn't it!



*SRX31929033: RNA-Seq of human brainstem tissue: uninfected control*

This is data collected from a regular sample of brainstem tissue. The study is "Dormant Mycobacterium tuberculosis in the Brain: Insights from Human Autopsies and a Murine Model". So it's not a tumor - I mean, I think Kassandra could still calculate the cellular composition, because the file is provided in the right format. But I'm looking trying to get a specific outcome.



*SRX31832122: Tumor RNA*

I changed the filter to "(fastq) AND "Homo sapiens"[orgn] AND (TRANSCRIPTOMIC) AND (tumor)". I added 'transcriptomic' to get the right type of data, and 'tumor' to get actual tumor data!

THIS one was promising - a bladder cancer tumor RNA sample from the "Field Effect-Informed Urine Liquid Biopsy Analysis for Assessment of Adjuvant BCG Response in Non-Muscle Invasive Bladder Cancer" study. 

***BUT***... it was locked behind the dbGaP (Database of Genotypes and Phenotypes) because it contained human sequence. I'm guessing a sample containing complete data on a human's DNA is grounds for restricted access.

But it WOULD have been great! All of its properties looked good - RNA-seq strategy, transcriptomic, and it even said "Captured libraries were sequenced using 2x150-bp paired-end reads on Illumina HiSeq4000 or NovaSeq6000" in its design - the same design as BostonGene's RNA sequencing: "Libraries were sequenced on NovaSeq 6000 as Paired-End Reads (2x150) with targeted coverage of 50 mln reads."

So yeah... restricted.

*SRX27190516: RIP-Seq of lung cancer*

Another miss, because of the strategy. RIP-seq is for something different. RIP.

*SRX31879952: RNA-seq of homo sapiens: clear cell renal cell carcinoma*

**Clear cell renal cell carcinoma is kidney cancer.**

This checks all the boxes. The thing is... *I still don't know if this is the right kind of data.*

Here are its attributes:

> Design: Poly (A) RNA from 1 mg total RNA or purified mRNA and purified m6A-containing fragments were used to generate the cDNA libraries, respectively, according to TruSeq RNA Sample Prep Kit protocol.

> Submitted by: Fudan University

> Study: IL8+ tumor-associated macrophages in ccRCC
PRJNA1405960 • SRP665132

> Studies on the function of the IL8+ tumor-associated macrophages population in clear cell renal cell carcinoma.

> Sample:
SAMN54758462 • SRS27835062
Organism: Homo sapiens

The reason I'm stuck here is mainly because it's open access. This is because I'm assuming that in real clinical cases, tumor samples are taken from patients directly, so their DNA is probably in the sample (tumor cells, blood cells, etc). A *real* sample of data containing complete information on a patient's DNA is grounds for privacy and restricted access, so why would this sample be available? I can't tell. Also, clicking on the 'SAMN54758462' sample says that the 'isolate' is "tumor sample of clear cell renal cell cancer treated with IL8 blockade". So on top of that, the description "treated with IL8 blockade" might mean it's not a normal tumor and the results will look weird.

Ok, so a couple things I've learned about these questions!

1. *"Why would a patient's tumor RNA-seq data be publicly available if it's supposed to be confidential?"* - THIS SPECIFIC TYPE of data - Cracked RNA strands - is one of the less sensitive types of genomic data. According to [this publication](https://pmc.ncbi.nlm.nih.gov/articles/PMC8326502/), the chances of re-identifying an individual from **transcriptomic data** are really, really low. Well, they're reassessing the risk because of new compute architectures and present-day hardware, but it's still considered low-risk so it can get put on public databases. 

2. *"'Treated with IL8 blockade'? Is that bad?"* - No bro. Tumor samples have different cell types in it anyway. This just means my analysis has to reflect the specifications of the data I'm using.

ChatGPT is like "bro, you're not trying to write a whole research paper. Just plug in the data and show results". But I AM trying. Because I GENUINELY CARE.

**I'm gonna use THIS one!**

### Downloading The Data

I downloaded SRA Toolkit from its GitHub repo. This is because the file exceeds 5 Gbases, and the SRA database doesn't allow direct downloads of files that big.

I extracted the folder in my Documents folder. Then in Command Prompt, I navigated to the `bin` folder in my new `sratoolkit` folder.

I ran `fasterq-dump --version` to check that it was installed correctly. It said `fasterq-dump : 3.3.0`, so we're good!

`fasterq-dump` is one of the SRA Toolkit commands in the bin file. It converts SRA files to fastq files. 

First, though, we need to download the SRA file. That's `prefetch`. It needs the **SRR accession number**, which is `SRR36909580` for our data.

> **Important:** It's 9/12 and I just caught that the SRR accession number is just the run number. It's not like a special passcode or anything, just a unique ID.

Here's what's gonna happen now: I'm going to download the file with prefetch. Then I'm gonna convert that file to fastq (unless it already is fastq?) with `fasterq-dump`. THEN, I'll have the exact same type of data that was used in the [initial study](https://ega-archive.org/datasets/EGAD00001008776) - bulk RNA-seq data from a tumor sample in fastq format!

#### Prefetch Download

I ran `prefetch SRR36909580` and it downloaded the file into a new folder. ezpz

I took a look at the contents of the file once I downloaded it - whoa dude! (I wouldn't recommend trying to display the file's contents, because I thought my IDE was going to crash when I tried. It got super slow on me. But you can try if you want to!) It's a ton of binary gibberish. But, there was one part at the start that had ASCII text. It was a bunch of lines like this:

`b53ccc62cc6568c424b587dd925cd1b0 *idx`

`69e4635827b25a3f8b1f4824142564f5 *idx1`

`d41d8cd98f00b204e9800998ecf8427e *idx0`

`870ff7fbd91df5cdb11cdf04cba1f718 *idx2`

Interesting how this file, the initial scan of a tumor sample's RNA strands, is structured like this. I'm also intrigued by this part... why are the 'idx' parts there? Are they indicating which libraries were used to map the reads? Maybe it has something to do with the technology - Illumina NovaSeq 6000 - that was used to sequence the RNA?

NOW to convert it.

#### Converting To FASTQ

For this part, it's important to note that I'm working with paired-end data. I'm pretty sure data can either be single-end or paired-end. The reason why this is important is because when we run fasterq-dump it'll give us *two fastq files* if it's paired-end. We gotta use both of them (in the right way).

So I ran: `fasterq-dump SRR36909580/SRR36909580.sra --progress`

This created two fastq files in `bin`: SRR36909580_1.fastq and SRR36909580_2.fastq. Awesome!

I'm not even going to try opening THESE files. They're way bigger than the SRA file - 9.8 GB each!

Now to use Kallisto. One more step towards Kassandra and my results.

### Using Kallisto

From BostonGene's website: "Kassandra uses the TPM expression of transcripts (gene isoforms) produced by Kallisto[1] as input. The Kallisto index file should be downloaded from the CGL pipeline repository (inputs, kallisto_hg38.idx) from the Toil project[2], whose results are hosted on UCSC Xena. This index file was built based on GENCODE transcriptome annotation version 23 (comprehensive gene annotation, regions ALL) and the human reference genome GRCh38 with genes from the PAR locus removed (chrY:10,000-2,781,479 and chrY:56,887,902-57,217,415)."

This means I need the data file and the index file to run Kallisto. I gotta use the same index file that BostonGene used, so the results are consistent.

*Why do we need this index file?* Good question! The index file is basically a library of transcripts that Kallisto uses to match each cracked RNA strand to a transcript. So you can see why using the same index file is important! Different transcript definitions would lead to different TPM values.

The index file is available [here](https://www.synapse.org/Synapse:syn5886142).

I'm just gonna move all of my files into the bin folder so I don't have to reference them all from different places. Wait, actually, I should download Kallisto first, then move them all to that directory.

Ok so I downloaded Kallisto, but from its [download page](https://pachterlab.github.io/kallisto/download). Thought I had to get it from GitHub but they also have precompiled binaries on this link!

I moved all the files I've been using so far into my new `kallisto` folder (also in Documents). Navigated to that folder in Command Prompt.

Then I ran the command:

`kallisto quant -i kallisto_hg38.idx -o output SRR36909580_1.fastq SRR36909580_2.fastq`

Let's see if this works...!

### Kallisto Results

IT WORKED BABY!!! We got an output folder with three things in it: an h5 file, a tsv file, and a "run_info.json" file. I got all three files I was supposed to! The .tsv file is really interesting to me because these are all supposed to be gene isoforms, and it's cool to me that Kallisto takes a bunch of broken RNA strands and can correctly identify which ones are active.

Let's check out the files in the text editor!

`abundance.h5` is just binary. Still cool!

`abundance.tsv` is both **understandable** and **awesome**. It's got 4 columns for each transcript:

> target_id

> length

> eff_length

> est_counts

> tpm

This is the output we need to plug into Kassandra - a TPM gene expression matrix.

**CORRECTION:** Ok so this is NOT a TPM gene expression matrix. This is *transcript-level*. It's a list of the abundance of each *transcript* in the sample. I think this makes sense because when I think about it, we're literally feeding cracked RNA strands into this algorithm, like broken up sentences, and Kallisto just turns it into the individual words it's supposed to be saying. Each transcript corresponds to a parent gene, sometimes different transcripts can have the same parent gene.

So this is *transcript-level*. We need to turn this matrix into a gene-level expression matrix. 

**KASSANDRA DOES THAT.** It takes a transcript-level matrix and turns it into a gene expression matrix *itself*. Then THAT goes into the algorithm part.

I would later figure this out from the programming part of the project. Looking into the core of the Kassandra code reveals a bunch of utility functions that do this exactly.

### Using Kassandra

We're finally here! Unfortunately, I can't use the online Kassandra tool because it's down for maintenance. And... what I thought was a "baby Kassandra" model on the GitHub was actually just a notebook that's used to TRAIN Kassandra... from scratch. Also it's the BLOOD model, not the tumor model!

Unfortunately, it looks like the project has found a very large roadblock. But it's not over - I'll just wait for the online tool to come back up.

I should probably use another tool. Just to get results for now.

For now, though, I wanna review what I've done and learned so far. There's a conference coming up and I wanna talk about AI innovation!

## Summary of Progress

Basically what I have so far is the file I need to plug into Kassandra. It's `abundance.tsv`, in the SRR36909580 directory.


## Outside Of The Project

All right so I've done some good stuff here. What other projects could be useful for medical companies? There was a study where Kassandra was used to compare TMEs across different cancer types - there weren't any significant differences, but the study used that outcome to infer a different place that could be causing the immune resistance. Maybe I could see how to help them in that study?


(3/2)

## MATLAB

Welcome back yall. I've got a lil friend here you're gonna love to see in a biomedical analysis project.

What I want to do now is prepare the data so that it becomes helpful. Kassandra did the same thing:

"As explained in the Kassandra study, transcripts belonging to several groups according to their biological types or quality of annotation and reference sequence are excluded from the TPM dataframe combined from the raw Kallisto outputs. Then the sum of expression of all retained transcripts is normalized to 1,000,000, which results in adjusted TPM values. Finally, each gene is assigned a TPM expression value by summing the TPM values of its transcripts according to the GENCODE transcriptome annotation (see figure below)."

So I want to emulate what Kassandra did. Their project isolated data that helped identify key things about the tumor sample.

So now the question is, can we plug a .tsv file into MATLAB and get some valuable knowledge out of it?



(8/3)

## Five months later

Ok so I ended up getting a contract job which is GREAT experience! I'm a little overwhelmed by my own movement, though, because I'm doing all sorts of things to get all sorts of jobs. Like I want a job at a hospital, or a laboratory, or a university, or a tech company. I wish these jobs were more stable.

So. I'm here at the step before I plug the data into Kassandra. Last time, I figured the model would be too large to train on my laptop. But it explicitly says I can train it on an average laptop. I figured I'd have to have a giant set of training data, though.

And as a recap: I've got the TPM gene expression matrix. Let's train the model, then plug this in to get a result.

## Training the model

### What do I even do

So basically Model Training.ipynb is a **documented example** of **training the model** and **performance testing**.

It's a notebook which is really useful for documentation, and in VSC I can execute blocks of code! But I was thinking I should probably just make it my own file.


(8/7)

Yeah so I've been looking for jobs again. I can't wait to be able to talk about this project with people...!

So what I'm doing now is looking at [this fork](https://github.com/jsangalang/Kassandra-modified) of Kassandra. It fixes bugs in their code, and provides better instructions for how to actually use it.

So let's get started! ML time baby.

On the fork, there's a couple instructions to get started. First is to set up a **conda** environment.

**Conda** is a tool that manages both software packages and isolated working environments on your computer! So with this, I can set up a special isolated environment for my work so it doesn't affect any of the other software elsewhere on my computer, and also install and use the correct software I need for this specific project.

Conda is the command-line tool for installing and managing. **Miniconda** is what installs this basic tool. **Anaconda** installs this tool and a suite of other cool software packages for data science and stuff.

USING Conda looks complicated. Just so you know, it's an **application** that gets installed. So you can look up "Anaconda" and "Anaconda Prompt" should pop up. That's it

**ERROR:** So I ran the `conda` command, and it gave me a bunch of "unsupported request" and "the following packages are incompatible" and "does not exist" lines. They're basic libraries like numpy and matplotlib too. 

**SOLUTION:** The environment.yaml file is a *Linux export.* That means that they don't exist for Windows at all! So I could either try running this from WSL, which IS Linux, so it supports these specs... or, I could write my own .yaml file that's for making this on Windows.

So I'm gonna write my own file because that turns out to be the *wwaaayyyyy* simpler option. Running this in WSL would mean I'd have to copy the file onto that virtual device, install conda there too, and then allocate more memory to it. I like Linux but I'm continuing on this "simplest" path.

> *What's a .yaml file?* 

It's just a file for readable formatting. Like markdown (.md).

> *Why do we need one?*

When we have a program that uses specific versions of packages like numpy, scikit-learn, and networkx, we need to be able to make sure we specify them so our program doesn't break.

> *How do I make a .yaml for my project to work?*

Basically, you look through the project for all of the packages that are imported. When you have that list, you disregard all of the ones that are already included in python or some other package, and other imports from the other parts of the repository. Then you'll list everything left in the .yaml "dependencies" list.

I made a new file called env-win.yaml to hold my Windows-supported dependency file.

It'll probably fail a few times after I run the `conda env create -f env-win.yaml` command.

*And that's how I made my own conda environment for running Kassandra supported by Windows!*


(8/9)

...Ok so my computer **CRASHED** from running that command. Huh???

I tried again and it gave an error - "Expecting value at char 0" in some file.

**So what happened here was** probably that my computer was already running a bunch of other stuff (Terraria, Chrome, Claude) and this *very intensive process* was too much for it. So the computer crashed. Now, when I retried the command, one of the files it needed was left empty, because the computer died while writing it. So.

I cleared the cache - `conda env remove -n kassandra` - and then removed the incomplete environment the first command half-made - `conda clean --all`.

So I ran this command a second time.

SUCCESS!!! It prepared, verified, and then executed the whole thing. Now I can activate it when I want!

### Machine Learnding

The first thing I noticed about the `Kassandra-modified` repository was that the example Python script both *trained* the model and *used* the model.

I want to train the model *first*, then *use* the same trained model to make predictions. Why would I want to train AND use the model every time? So, this means I have to save the state of the trained model somehow.

Here's what I did in the repo:

1. In `kassandr_model_training_example.py`, I copied everything before the "Model prediction with datasets" comment, and pasted it into its own python script file.

2. In that file (`train_kassandra.py`), in the "Model training" part, I changed the num_points value in the SECOND `mixer` declaration from 300000 to 3000, to make the training process way faster (for now).

3. This is where I'm adding the "save the trained model object" script. I imported `pickle` and `pathlib` so I can store the object with pickle and save it to a specific place with pathlib. The current program doesn't save the trained models, so I'm making sure it does.

4. I added a snippet to *load* the trained model into the `predict_kassandra.py` script with the pickle library.

Now we're here before the training step.

(8/23)



Ok, a few days later. I'm about to activate the conda and run the training script. A couple concerns though. The model is trained on cell types, right? I think somewhere it said that there are different models for blood and tumors or something, and that's because some cell types aren't included in one. Just wanna document exactly what that was. I'm training the tumor model right now, it looks like.

**CORRECTION:** *I'm training the model on the same dataset that the production model used in its paper.* That dataset is the *cell profiles* of thousands of samples from patients with tumors, which are sorted cells. *There aren't separate models.* **THE THING THAT CHANGED** is how many artificial transcriptomes are generated on my computer *right now*.

**CORRECTION TO THE CORRECTION:** There *are* separate models. When you 



Also, understanding the program. It looks like LightGBM is used as the machine learning library. Why this one? Why not pytorch?

*It's because of the type of problem!* Our goal is tabular regression - predicting a pattern using this table of gene expressions. There's no locality, though. Nearby genes probably don't relate to each other at all. Gradient-boosted trees as used in LightGBM are the default for these tasks.

Hmmmmmmmmmm is there anything else I need to document or fix before training. 

Let's just do it. I also want to have a direct way to test if my results are good at all. The example ipynb has a "Performance testing" section where it runs the model on some example data. It provides the data and the resulting graphs from the test. So once I train the model, if I test it on `dataset = 'GSE107572'` and my graphs look similar to theirs, **I'M ALL GOOD BABY!!!!!!!!!!!**

### Training (finally)

I activated the conda environment and ran train_kassandra.py! The whole process took ~4 minutes.

It gave a bunch of these errors though:

> [LightGBM] [Warning] No further splits with positive gain, best gain: -inf

> [LightGBM] [Warning] Stopped training because there are no more leaves that meet the split requirements

Not to worry though! These are just how LightGBM fits its data.

Let's test the new .pkl file we got by writing a `test_kassandra.py` script.

## Testing the trained model

### Two bugs fixed

We have a new .pkl object in the models/ folder. I'm gonna copy the first "Performance testing" part of the notebook and add the correct imports so I can replicate that and see if my model produces similar stuff.

(I also copied the necessary data I need for this into this repo. We're doing the GSE107572 data, so I copied both of those .tar files from the official Kassandra repo into the data/ folder.)

**Error 1:** Running it gave an error originating inside the `core/cell_types.py` methods. Specifically, in the "line 116, in __getattr__ > return self._types_dict[item]" line. It kept failing at that point.

I asked Claude and it suggested changing the __getattr__ method in that file, because it didn't account for when __init__ was never run. This is probably because we're loading the model from a pickle file. So I made the change.

**Error 2:** I ran it again. ANOTHER error. Progress!!! This time it's in `core/plotting.py`. No biggie, it was probably just a matplotlib version mismatch. I changed "ax.grid(b=False)" to "ax.grid(False)" and that worked.

So I ran the test script again and it all went through, no errors!

I added plt.show() at the end of the test script to show the graphs. I changed plt.rcParams['figure.dpi'] = 200 to = 80 because the text was super big and crammed together.

So now we ACTUALLY HAVE RESULTS!!!!!!!!!!!! Awesome job me!!!

The plot from the notebook and the plot of my result are verrry similar. Mine has a little variation, and the pink points in the notebook's plot are missing from mine.

Looks like I'm good to continue!



(8/27)

## Using the trained model

So now that it seems to work, I have to use my model on the abundance.tsv file I got from the publicly accessible dataset. This sample is "RNA-seq of homo sapiens: clear cell renal cell carcinoma" (SRX31879952 on the NCBI SRA database). So I have to account for any special attributes of this sample, like what "treated with IL8 blockade" means.

(I had to copy files over again. This time, to actually run the predict script, we need `genes_in_expression.txt`, `id2gene_gencode23_uniq.txt`, and `tumor_model_transcripts.txt`)

*So I ran it*, and it made a new `deconvolution_percentages.tsv` in my output/ folder. It looks great! Right now, though, my script only makes that new file. Also **it overwrites the same file on every run**. Lemme add the same code we used to make graphs from the data so we can save the results

...It turns out I might not have the files I need to make the same types of plots as the testing example. I want to plot this info, but it looks like the test examples had an `expr.tsv.tar.gz` file and a `cytof.tsv.tar.gz` file to plot with. Looks like these are the files for the *actual* cell composition, because the test graphs are predicted cell % vs actual cell %. I don't have those for my input file.

Which is fine. That just means I can't do that type of plot for this sample. Um, I can plot something else. What to plot, what to plot.



## Results

1. I got a couple plots from using the provided example datasets. 

So that's something. This actually verifies that my model works. So I guess this just completes the *technical* part of the project.

2. I got a *cell composition % table* from running Kassandra on my own dataset. 

This is the part that tests the *oncological* outcome of the project. I need to use this to demonstrate how this *helps*. Like I've got the data, sure, but what do I even do with it?? I feel like I need to be a doctor myself to truly complete this part of the project - maybe that's just perfectionism, but at the same time, I have no idea what most of these words and acronyms mean. 

### FOINALLY posting this thing

I want to FINALLY POST THIS REPO. I shoulda posted it a while ago! But now I've got **A RESULT** from the thing and I can talk about it.

So what I'm going to do is post 
- this log,
- a more concise README for the specific process, 
- the .yaml I made,
- my scripts, 
- my fixes to the code,
- my output and results, and 
- the license.md that jsangalang has on their fork because that gives credit to BostonGene and it's part of the algorithm's license agreement. 

In my *own* repository. I'll call it "Kassandra Analysis and Testing Project".

Thinking about leaving the results section basic for now, and just emailing Dr. Fowler like “hey I got this and idk what to make of it”. 

In the same room, I noticed on the NIH SRA database site that when I go to the SRX31879952 page, it has links to other things with different IDs. Different sections - “Sample”, “Study”, “Runs”. The sample has a “SAMD” ID, and clicking on it leads to its page, which also has a familiar BioProject “PRJNA” ID link, which leads to all of the samples for this project. And there are several more.

Wow. So the database individually contains experiments, projects, samples, and um, runs? I just clicked on the “run” ID link to get to the sample I downloaded - since there’s only one link, I assumed there was only one tumor sample. But it seems like this page is describing the *one* experiment that used this *one* sample in the *collection* of experiments of the bigger project at hand.

So every project (PRJNA) can have multiple BioSample specimens (SAMN), one specimen can have multiple experiments done on it (SRX), and one experiment can have multiple *runs* - from the technology - for reading the data.

Anyway maybe I could take these other samples (if they’re very similar, since they’re in the same project), run them through the pipeline, and plot their results together to display something useful.



(8/30)

So now that I've finally posted something I can show and talk about, let's make that LinkedIn post. I made a section about it a while ago after I did the Kallisto step - I'll just move it here.

## LinkedIn Post

BostonGene is pioneering the integration of predictive modeling in clinical research. Kassandra, a machine learning-based algorithm that predicts the cellular composition of tumor samples, is their novel contribution to stepping oncology research forward.

I've illustrated the pipeline of data that researchers use to generate raw tumor RNA samples into a generated reconstruction of the TME in an easy-to-understand format, and tested the programs used to normalize and extract knowledge from the data. My findings include [fill in after testing Kassandra]. The work by @NathanFowler and the BostonGene team inspired me to complete this project.

Could predictive modeling become the industry standard for clinical practices? I'd love to see it happen first-hand.

> #Oncology #MachineLearning #BostonGene #Research



(9/4)

## Studying oncological background

I guess I should start from the ground up.

This whole program was started to help doctors choose a therapy method for patients with tumors. Right?

I studied this interview by **Alexander Bagaev**, Chief Product Officer at BostonGene. When asked about the history of BostonGene, he said it started with a brainstorm session to figure out what they needed to study in order to accurately diagnose tumor patients with a treatment therapy that *doesn't not* help.

He also said a bunch of other cool things that I'm excited to talk about with him like how he's deciding which patients are good to test drugs on, the other benefit of BostonGene's products. And also the **interpretation disconnects** between physicians and hospitals!

---

**PERSONAL NOTE**

I sent another email to Dr. Fowler updating him on my progress/status. He finally responded!!! He said my project is impressive and told me he's getting in touch with Dr. Bagaev. DUDE THIS IS AWESOME!!!!!!!!!

So I did a bunch of research into Dr. Bagaev's background, his role/history, his research papers, and all that good stuff. This interview came up on LinkedIn - they turned some parts into little Instagram-esque clips.

His background is super impressive too. He wanted to be a theoretical physicist at first (very cool, because I study quantum info theory), graduating in Moscow in physics, and aspired to apply math to biology to help healthcare. He joined the company early when there were only 10 people; it started as a cloud-based company that did "dry labs", just handling raw data and researching how to best make use of it for healthcare. He's seen many parts of BostonGene's operations; he was a bioinformatics analyst, then a team lead, then worked his way up all the way to CPO. 

---

So anyway, BostonGene aims to use multimodal data to develop both *drug development* and *clinical diagnoses*. The diagnostic space is, quote, "cumbersome", because apparently hospitals that receive BostonGene's products *don't fully understand* how to *interpret their results* as useful knowledge.

**That's what I'm focusing on here.** How can I interpret the cell composition % table I got from Kassandra? What is it telling me? How would I get from that to a favorable treatment modality?

Well. I'm looking at something very specific here. I'm not a doctor or an oncologist.

But hey I'm 24 and I have today off from JCPenney.

So let's start from scratch. BostonGene wants *drug development* insights and *clinical diagnosis* insights. Let's study the diagnosis part.

...

Watched "Principles of Cancer Treatment" on YouTube (9 years ago). Great! Very general idea acquired.

Ok lemme slow down. Now that I think about it... it wouldn't make *sense* for me to be able to select the "correct" treatment modality from *THIS* point, where all I have to make this decision is the predicted cell composition of the tumor. Treatment selection has lots of different factors to consider based on the tumor, the patient, and the many different available treatment options.

So... what now? 


(9/10)

All right so BostonGene just presented two new abstracts at SOHO 2026, a conference here in Houston. Wish I coulda been there (I totally woulda helped them set up their booth or whatever they needed but it costs 100 bucks to get in). One of the abstracts was an **actionability score for targeted therapy selection**. 

DO YOU KNOW WHAT THAT MEANS!?!? IT MEANS THEY'RE DOING THIS WHOLE ENTIRE THING!!!! They made programs for genetic classification and cell composition prediction, and now they're making the framework for **HOW TO USE THIS INFORMATION** in clinical settings.

I think that's what BostonGene is focusing on right now. Making a *framework* for how to get from what they have to **what it means** and **what they should do about it**. 

I'm writing this because I'm trying to mentally prepare for my meeting. There's a central question I'm faced with. *What am I interested in about BostonGene?* (I'm overthinking a little bit here because I'm nervous.) I'm interested in the research and bioinformatics part of their work. 

So how would I contribute to that? Realistically, all I've done so far is *use* their product. How would I take it forward?

I originally wanted to improve the algorithm somehow by making it a hybrid quantum-classical approach. But I don't think this is the kind of project that needs that. Like, *what part* would I apply it? I read their original Kassandra paper.

I think the best thing I can do right now is continue the project. I gotta confirm the m6a thing, then do the other samples, then plot them in some way. Also I can research what the percentages of cells can actually tell us once I have the plots.


(9/11)

## Project Part II - Electric Boogaloo

Ok so the main goal is to get the rest of the SRA database samples (from the same project) plugged in to the same pipeline I did with the original sample I chose. The cool part that I didn't see before is that there's *control* samples and *IL8* samples, so **the LEAST we can get from this project is a comparison of the tumor microenvironment cell composition before and after IL8 blockade treatment**.

That means I'm gonna have to download a buuuuuunch more GB of data (that probably exceeds my laptop's 1TB storage). No problem, though. I can trash whatever I don't need anymore after processing. I'm just gonna have to do it all in batches.

### Verifying the data (annoying)

There was an issue Claude caught with the type of library the experiments are using to read data from, so I wanna explain why it's significant.

> The issue: "Is this data really an RNA-seq read of a tumor sample, or is it something else?"

I recently learned that the NIH SRA database is a lot more comprehensive than I thought when I first used it to get my sample. As I wrote earlier, it connects whole projects, their experiments, their samples, and the runs used to measure the sample data. The point of conflict here was the "Library" section of the experiment and its details. Here's some more context!

**Next-generation sequencing (NGS)** is an advanced laboratory test that reads the genetic information of a tumor sample. That's what the HiSeq X Ten machine does, and that's how we get from a tumor sample to an RNA-seq read which we can use (in bulk) to study the tumor's mutations and stuff.

The information that the sequencing gives you **DEPENDS ON THE LIBRARY YOU PREPARE FOR IT.** A **library** in an NIH SRA project experiment is a collection of DNA or RNA fragments collected from the biological sample you want to study. So the library is LITERALLY the **physically prepared** sample. You can't really say "sample" and "library" interchangeably because the sample gets prepared and *becomes* a library. Annoying lab lingo.

- The "physically prepared" part is super important here. That's preparing the library. Earlier I was confused if a library was some outside reference that the machine used to map the molecules read from the sample to some set of genes. Then I convinced myself that the sequencing machine (HiSeq X Ten) was the thing that selectively scanned the input sample's DNA/RNA strands based on that reference. ***Nope!*** The HiSeq X Ten is gonna read whatever molecules are put in it. *How you prepare the sample* determines *what goes into the machine* and therefore *what data is collected*. 

There are a few different ways to prepare a library. 

The SRA `PRJNA1405960` project used **PCR (polymerase chain reaction) selection**. I read this Thermo Fischer Scientific article about the different types of sequencing, and PCR was in there as a type of *targeted sequencing*. BostonGene mentioned using switching from whole genome sequencing (WGS) to this in order to study the TME and see what the tumor is immune/resistant to; it doesn't require inputting the whole genome, so I figured this was a method of narrowing the input data. The way I understood it, I thought this was a type of "data filtering" method that only focused on the select molecules in the tumor sample.

***************Nope!***************

PCR is just copying DNA.

PCR IS JUST. COPYING. DNA. We're just duplicating the stuff so we have more of it. BRUH

 So really, it doesn't do anything for the project but make the sequencing machine more accurate. It didn't select only certain parts of the transcriptomes, and it didn't filter any genes or other data out. It just made the whole sample a little clearer - I imagine PCR happens a lot in these types of experiments where you're handling DNA/RNA. Jesus it took ONE google search - "what does pcr amplification do" - and it all clicked.

So the **REAL** answer for "is this library really giving pure tumor sample data" lies in more than just the `Selection: PCR` field. The "Library" section of the experiment page tells you a lot more about how the sample is used. The "Selection" field **IS NOT TARGETED SEQUENCING!!!** It just tells you *how the researchers isolated, filtered, or captured the subset of DNA/RNA that actually ended up in the sequencing machine.

I'm sure I wrote this earlier, but here it is again. The "Strategy" field is telling us that we're getting normal RNA-seq data. Other strategies *would* filter data out, but this is simply scanning the entire library for every single cracked RNA strand it contains. Just like what an RNA-seq file is supposed to be. The "Source" field also says `TRANSCRIPTOMIC` so that tells us this gives us transcriptome-level data (again, exactly what we need for Kassandra).

**CONCLUSION:** I just had to make sure this was normal bulk RNA-seq data. ****It is.**** The "Strategy" and "Source" fields of the library confirm it.

I just confused myself because I wasn't sure what "library" meant, then I read an article about it and thought the Selection field was a *wayyyyy* bigger problem than it actually is.

### Useful info

The samples were actually *ex vivo*, meaning treatment was done to tumors in a lab, not in a patient directly. Really interesting! Oh btw [here's the DOI](https://doi.org/10.1158/1078-0432.CCR-25-4384) for their study.

**Side note:** Just thought of something. I should make bar graphs for the actual cell composition datasets of all of BostonGene's provided examples. This'll give me a good idea of what the cell composition should generally be in a tumor sample.

---

### SOHO 2026

Oh my god I'm here. I spoke to a couple different booths! But **BOSTONGENE ISN'T HERE.** They basically just presented their abstract on September 9 and left.

***NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!***

It's fine, I can still network. I spoke to a couple different people (the people at Sumitomo Pharma were super chill and offered to connect me to an MD) and got some pamphlets and papers and water and snackies.

I got an Insider magazine that has a copy of the SOHO program, as well as articles explaining the central topics. Super useful - will come back to this later.

I think I'm throwing people off by being here. Sometimes people think I'm younger than I am. And I don't have a nametag, which everybody else has. And, obviously, I talked to the booth presenters and they explained their, uh, stuff to me, and I listened, and *really, genuinely tried* to understand and ask good questions. I tried. But again I'm not a doctor.

But: #gameisgame

**Bristol Myers Squibb** had a booth with some interactive touchscreens showing their commercial/research stuff. What I saw interested me. I can't remember the specifics right now but they had the words "target" and "protein" in it. Excuse me??? Did you say *quantum*??? I'd love to see if I can apply it there. An ambitious long shot, but quantum computing is super interesting to me and I wanna get involved there somehow. Maybe I can do a project on their products too.

*I FOUND THE PRESENTATION ROOM!* It's an auditorium and a bunch of doctors are presenting their studies. I'm seeing some familiar names - Dr. Chamoun's name is in a presentation's citation, I met him at the TMC AI Summit.

Terms that keep getting repeated that I should probably keep in mind:
- CAR T cells
- Therapy selection
- Liso-cel
- BTK degraders

I liked Dr. Westin's presentation - he, as well as most other presenters, targeted the question of how to select therapy modalities in his presentation. I tried talking to him about it - I introduced myself and started asking. But he was trying to listen to the next presenting speaker, and he told me to send him an email. I sent him a LinkedIn request.

The connection to the Sumitomo Pharma presenter made it worth it - not only did he offer me a referral, he *encouraged* me. I should follow up with him; we're connected on LinkedIn now!

---

### Preparing to use Kassandra (again)

Let's run a couple more tumor samples through Kassandra so we can compare the IL8 and control groups!

**Run Selector** is cool. It's a feature on the NIH SRA database that lets you find all of the runs that were collected in a select project. You go to the BioProject's page, then in the "Project Data" section, click on the number of links for SRA experiments. That'll take you to the page displaying a list of experiments for the project, which has a "Send to..." dropdown in the top right. Use that to send it to the Run Selector!

The Run Selector displays pretty much all the info for all the runs. The thing I'm looking for here is how I'm going to notate and organize my data. I'm thinking I'll download the sample pairs they named as "Sample 1", "Sample 2", and "Sample 3". So I'm using the `Sample Name` column to decide which samples I'm downloading.

The **control samples** I'll download are:

| Sample Name | Run ID | Experiment ID | File Size |
| -------- | -------- | -------- | -------- |
| S1  | SRR36909605 | SRX31879927  | 1.83 Gb |
| S2  | SRR36909593 | SRX31879939  | 1.89 Gb |
| S3 | SRR36909585 | SRX31879947 | 1.84 Gb |


The **IL8-blockade-treated samples** I'll download are:

| Sample Name | Run ID | Experiment ID | File Size |
| -------- | -------- | -------- | -------- |
| S1_IL8  | SRR36909604 | SRX31879928 | 1.84 Gb |
| S2_IL8  | SRR36909586 | SRX31879946 | 1.87 Gb |
| S3_IL8 | SRR36909584 | SRX31879948 | 1.88 Gb |

I'll start with these. Gonna see how long it takes. Will trash all the input after I get the Kassandra cell composition % prediction, because again, space.

Downloaded SRA Toolkit - the compiled binaries from GitHub. Added the extracted `bin/` folder to PATH.

> **Important:** When I downloaded kallisto last time, I didn't download it in the right place. When I install a command line program, I want to be able to use it from anywhere. What happened last time was I extracted the program in my Documents folder and didn't add it to my PATH properly (The PATH environment variable lets you use programs without having to navigate to the directory that the program is in). So I ended up moving all the files to the folder WITH the program and running it that way. *Obviously that's kind of annoying.* So here's what I'm doing THIS time: I made a folder called `tools` in my user folder, and extracted the sratoolkit compiled binary .zip into THAT folder. THEN: I added the `bin` folder's path to my PATH environment variable. That worked.

> And you can do the same thing with kallisto!

Downloaded kallisto compiled binaries from the Patcher lab Downloads page. I got the program from bin and moved it straight into the `tools/` folder. Added the `tools/` path to PATH. (It's a single .exe file, so it's fine if I don't have it contained in a folder like all the SRA Toolkit .exe's.)

Downloaded the index - `kallisto_hg38.idx`. I had to use one of my limited authenticator codes. I tried signing in with my Google account but idk where it sent the 2fa code. Whatever. Not like I'm gonna download it 9 more times...

Now I've got everything I need to download my data. Hold on, lemme organize everything...

### Organizing everything

Here's how I'm structuring this part of the project. My local `runs/` folder is where I'm going to be downloading the data with prefetch. I'm converting these to fastq files *in the same folder* with fasterq-dump. I'll then run them through kallisto to store the resulting TPM transcript matrices. **This step** is going to make an output folder with the abundance.tsv we need to plug into my `predict_kassandra.py` script. I think I might have to make a modification to the predict script to put the output (cell deconvolution) in the `output/` folder. Nope it already does that I just have to make it a dynamic filename using the unique SRR ID

- I'm making the `runs/` folder locally, and I won't upload them because again I'm trashing these when I'm done with them. The idea is to do all of this in one location so that I don't have to move gigabytes of files around! I'm NOT DOING ANY OF THIS WORK IN THIS REPO. After I'm done I'll copy over the updated script, then move the deconvolutions to this output/ folder.

- Also I'm going to store the kallisto_hg38.idx index file in a folder in the other repo called `index/`.

Oh... I forgot running Kassandra needs both the preprocessing data and core/... **so HEY YOU, do this in the Kassandra-modified folder.**

So it's constantly keeping the run ID through every command and it works in its own folder. Therefore, no problem mixing up abundance files or anything!

Two changes to predict_kassandra.py: Allow passing the run number as an arg, and put output in output/, **oh and also** make sure it's not overwriting to deconvolution_percentages.tsv *every time*, because right now it's just `preds_df.to_csv('output/deconvolution_percentages.tsv')`. Once we pass args we can use that to name the outputs accurately. Cool!

I'll probably also make a .bat file that does this whole thing for one run. I'll run one sample manually so I can document the commands are right, then write the .bat.

### Replicating the download -> deconvolution process

So let's start with "S1" - our first control sample!

Now running `prefetch SRR36909605` **IN THE RUNS/ FOLDER**.

It makes a folder with its SRR ID in runs/. Awesome.

Running `fasterq-dump SRR36909605/SRR36909605.sra --progress` **ALSO IN THE RUNS/ FOLDER**. This made the fastq files in runs/ instead of the SRR~/ folder. Ok, so I guess in the future I should go in the SRR folder for this step.

Running `kallisto quant -i C:\Users\adolf\Desktop\Kassandra-modified\index\kallisto_hg38.idx -o output SRR36909605_1.fastq SRR36909605_2.fastq` after moving those files into the SRR folder **and navigating into it**.

All right so where the files are being made is a big deal here, well, to me, because I wanna organize this whole thing. Running kallisto gave its results in an "output" folder, but I'm gonna rename it to SRR36909605_quant to indicate that this is the kallisto output. This'll be automated in the .bat as `%SRR%_quant`.

Oh... I forgot we need to run our python script in conda. Can we automate that...? *Yes, we can.* I manually activated the conda environment in Anaconda Prompt and ran the predict from there just now, but automating it involves stating the path to the conda environment's `python.exe` and using that to run in the .bat.

### Automating the the download -> deconvolution process

All right! Now that we've got the whole process, we can make our .bat.

The paths are the main issue here. Once I upload it I'm gonna specify to change specific path names.

Let's test it out on "S2", the next control sample.

Ok so in the Kassandra-modified repo, I actually didn't put my python scripts in a scripts/ folder, so it failed on that step. But I went to the Anaconda Prompt and did it manually again because the rest of it worked. Fixed the .bat. I'm sure the placement/paths issue will fix itself once I copy over my changes.

~~I'm also manually renaming my deconvolution files to add the sample names at the beginning of their names. So I can know what I'm plotting later!~~ Oh you know what, why don't I just get that **giant table of sample run data from the Run Selector?** Ok I downloaded it in a csv, all fields are separated by commas, so that's what I'll use to plot/sort/name data later.

So let's test this .bat version on S3.

Perfect it worked! It put everything in the right spots and it removed the big fastq and sra files I don't need anymore.

### Making a plotting script

I wanna plot this data after I get the rest of the samples processed. Right now I'll just try plotting the percentages of the first 3 samples.

**What to plot:** I'm assuming all I have to plot is the cell percentage of each type of cell in the samples.

BostonGene's first example performance validation dataset, GSE107572, plotted only 7 of the types of cells in their .yaml file. I want to plot all possible types, so that interpreters of this project's results aren't missing anything.

> Note: Some of the objects in cell_types.yaml are part of other objects. Like for example the percentage of Lymphocytes can be plotted as the sum of B_cells, T_cells, and NK_cells percentages. BostonGene did this in their validation plots.

So here's the leaf nodes in the tree of cell types, which I'll include in my plots!
- NK_Cells
- Monocytes
- Macrophages
- Endothelium
- Non-plasma_B_cells
- Plasma_B_cells
- ~~Granulocytes~~ (Removed in fork)
- CD4_T_cells
- CD8_T_cells
- ~~Dendritic_cells~~ (Removed in fork)
- Fibroblasts

The plots would be `Cell Type` (x-axis) vs. `Predicted Composition %` (y-axis).

**How to plot it** is what I'm trying to figure out now. There's an optimal type of graph I need to create to display the information most effectively. 

Maybe a bunch of little paired bar charts, one for each sample pair? Because I've got 7 different groups of cells I'm plotting, and they're all mutually exclusive, so lines aren't the play. It would be helpful to pair *one sample's* control and IL8 together directly, to clearly and directly see any differences.

Not sure how to plot *all* of the data in one graph. Maybe I don't need to.

What I *do* know is slope charts look cool. Maybe that would work for all of the data? Left would be control percentages, right IL8 percentages. Then the lines would be color-coded based on cell type, and the slopes would indicate the change. Damn am I becoming smart?

### Plotting the Kassandra tables for 3 pairs of samples

So I ran a quick plotting script Claude made and they're verrrry similar. The problem ended up being which column of the deconvolution.tsv table it was selecting from. I changed `iloc[:, 0]` to `iloc[:, 3]`, and it worked like a charm!

*Now* we have plots displaying a *real difference* in clear cell renal cell carcinoma tumors before and after being treated with IL8 blockade.

The script still has some issues I'm trying to fix. 

Also I still need to download the rest of the data.