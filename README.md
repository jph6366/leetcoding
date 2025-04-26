# LEETCODING

A repository for solving and summarizing coding problems in preparation for technical interviews.
I explore different facets of study aids for coding interviews and document the process for the next struggling code-monkey.

KEYSTONE TECHNIQUES AND TALENTS
- SPACED REPETITION
- GRADUAL PROGRESSION
- BORING VARIATIONS

## HARTMAN PROFICIENCY TAXONOMY

1. FAMILIARITY: recognizing flows, mental models, and patterns
2. COMPREHENSION: discussing the patterns
3. CONSCIOUS EFFORT: experimenting and learning through trying everything
4. CONSCIOUS ACTION: mastering the pattterns by knowing what to try
5. PROFICIENT: finding and manipulating unseen patterns
6. UNCONSCIOUS COMPETENCE: simple

## FLASH CARDS

I sought out some reviews of the flash card softwares out there because I find the manual handwriting of flash cards to be unproductive, especially since the actual coding is done on a screen! Fortunately white board technology has been invented to aid in handwriting concepts much easier, but we lose the repetition quality the flash cards offer. This repetition is better known as spaced repetition, learning technique based on increasing intervals of time between subsequent review of the learned material. 
 - **SuperMemo (from "Super Memory")** is a learning method and software package developed by SuperMemo World and SuperMemo R&D with Piotr Woźniak in Poland from 1985 to the present.
    - They have archived a lovely list of bullet points chronologically depicting the [History of SuperMemo](https://super-memory.com/english/history.htm), which reads from Hermann Ebbinghaus's Forgetting curve (1885) => Robert Bjork's theory of disuse (1969) => to finally Piotr Wozniak's computational spaced repetition, i.e. the technique in which knowledge is reviewed in optimum intervals that are determined by a computer with the goal of reaching a desired level of knowledge retention. 
        - For a detailed description of the first algorithm see: [Using SuperMemo without a computer](https://super-memory.com/articles/paper.htm)

 - **Anki** is a free and open-source flashcard program and implements the SM-2 algorithm, read more on the [SuperMemo algorithm (SM-2)](https://en.wikipedia.org/wiki/SuperMemo#Description_of_SM-2_algorithm),
    - The SM-2 algorithm in Anki been modified to allow priorities on cards and to show flashcards in order of their urgency. Anki 23.10+ also has a native implementation of the Free Spaced Repetition Scheduler (FSRS) algorithm, which allows for more optimal spacing of card repetitions.

**So which is software and algorithm implementation is better?**
- SuperMemo currently uses [SM-18](https://supermemo.guru/wiki/Algorithm_SM-18) and its hard to find a definitive answer due to the nature of the validity for metrics of proving one's ability for retrieval and retention (but there is a technical comparison for [SM-17 vs. older SuperMemos](https://supermemopedia.com/wiki/Algorithm_SM-17_vs._older_SuperMemos)).


Below is a graph of the result of simulation that SM-17 is better than SM-2
(pulled from https://www.masterhowtolearn.com/2018-11-11-my-comparison-between-anki-and-supermemo/)
![SuperMemo2vsSuperMemo17](./doc/spaced_repetition_algorithm_contest.png)

"The least squares metric for Alg SM-2 equals ~54% as compared to ~37% for Algorithm SM-17. This does not sound like a lot, but it may easily double or triple the review workload (esp. for shorter intervals).”

- Based on this we can say in the long-term SuperMemo is superior, although it simply locked to Windows making it hard access and manage on my GNU/Linux Desktop. I will be using Anki (on Ubuntu 22.04) with a modern spaced-repetition scheduler, which you can check out here at [FSRS4Anki](https://github.com/open-spaced-repetition/fsrs4anki).

...

## SYSTEM DESIGN

...
