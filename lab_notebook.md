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

"A collection of more than 18,000 bulk RNA-seq, covering numerous immune and stromal sorted cell populations and cancer cell lines, was curated using the GEO and ArrayExpress databases (Barrett et al., 2012). The raw RNA-seq datasets were combined, homogeneously annotated, and bioinformatically recalculated for comparable measurements of transcript expression within each cell type to reduce batch effects. After quality control, well-defined cell clusters were revealed, populating the Kassandra sorted cell compendium with purified RNA-seq samples (n = 9,404) of diverse immune and stromal cell populations, including malignant cells from 24 cancer types (n = 2,166) (Figures 1B, S2A, and S2B)." (Fowler, et al., 2022)

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

From the study: "A collection of more than 18,000 bulk RNA-seq, covering numerous immune and stromal sorted cell populations and cancer cell lines, was curated using the GEO and ArrayExpress databases (Barrett et al., 2012). The raw RNA-seq datasets were combined, homogeneously annotated, and bioinformatically recalculated for comparable measurements of transcript expression within each cell type to reduce batch effects."

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

### Using Kassandra

We're finally here! Unfortunately, I can't use the online Kassandra tool because it's down for maintenance. And... what I thought was a "baby Kassandra" model on the GitHub was actually just a notebook that's used to TRAIN Kassandra... from scratch. Also it's the BLOOD model, not the tumor model!

Unfortunately, it looks like the project has found a very large roadblock. But it's not over - I'll just wait for the online tool to come back up.

I should probably use another tool. Just to get results for now.

For now, though, I wanna review what I've done and learned so far. There's a conference coming up and I wanna talk about AI innovation!

## Summary of Progress

Basically what I have so far is the file I need to plug into Kassandra. It's `abundance.tsv`, in the SRR36909580 directory.

## LinkedIn Post

BostonGene is pioneering the integration of predictive modeling in clinical research. This is important because it "will lead to an improved understanding of the tumor microenvironment, which is a critical factor in cancer pathogenesis, clinical outcome, and therapeutic resistance" (BostonGene, 2026). Kassandra, a machine learning-based algorithm that predicts the cellular composition of tumor samples from bulk RNA-seq data, is BostonGene's novel contribution to stepping oncology research forward.

I've illustrated the pipeline of data that researchers use to generate raw tumor RNA samples into a generated reconstruction of the TME in an easy-to-understand format, and tested the programs used to normalize and extract knowledge from the data. My findings include [fill in after testing Kassandra].

Could predictive modeling become the industry standard for clinical research? I'd love to see it happen first-hand.

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

**CORRECTION TO THE CORRECTION:** There *are* separate models. 



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

I got a couple plots from using the provided example datasets. So that's something.

### FOINALLY posting this thing

I want to FINALLY POST THIS REPO. I shoulda posted it a while ago! But now I've got a **RESULT** from the thing and I can talk about it.

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

