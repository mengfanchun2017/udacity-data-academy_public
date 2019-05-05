# 机器学习纳米学位毕业项目（恶毒评论）v2

> 项目问题，请老师指点：

**问题1：**Kaggle 在给出 Test 数据时为什么要披露条目是否是恶毒评论或是正常评论。（问题在项目中有详细说明）
**问题2：**目前看需要使用AWS GPU主机进行项目的分析，因为时间非常紧迫（还有3周，对AWS不熟悉），想问下：**如果使用迁移学习的方法，这个项目可能在没有独立显卡的笔记本跑完么？**
**问题3：**请问老师多分类的情况用什么可视化展示比较好。（这种情况用什么可视化展示比较好？（问题在项目中有详细说明）

> 20190418 v2 修改稿

评审老师好：
根据反馈，修改的地方如下：
1. 学生清晰的描述了需要解决的问题。问题被明确的定义出来并且至少有一个可能的解决办法。此外，还要求这个问题可以被量化，被衡量以及可重现的。）
    1. 根据反馈增加了 _具体指出该多分类问题的特点的相关内容。_
    2. 该任务是一个标签不平衡的文本多分类问题，并且每条数据可能对应不止一个标签。
    3. 已经修改。
2. 学生提出了一个用于量化基准模型和解决方案的评估标准。这个评估标准对于问题本身、数据集以及解决方案来说都是合适的。
    1. 评审老师反馈使用，mean-auc 评测。找到了相关的说明[^mean-auc]。指的是： `the score is the average of the individual AUCs of each predicted column.` AUC 进行评估的说明更新在了项目相应部分。
    2. 已经修改。
3. 学生总结了一个针对问题解决方案的实施理论流程。探讨了计划采取的策略，对数据需要进行哪些分析，考虑哪些算法。这些流程和探讨符合该问题的特点。我们鼓励把数据简单可视化，加入一些对解释有帮助的伪代码及图表。
    1. 传统词袋模型参考课程链接中的第一个模型：[^wordbag]
    2. 已经修改。
4. 文本跟新说明
    1. 本版本根据反馈更新，并为了可读性对于模版中的要求进行删减。

[^wordbag]: [词袋模型 + LR 解决方案(Kaggle)](https://www.kaggle.com/tunguz/logistic-regression-with-words-and-char-n-grams)
[^mean-auc]: [Jigsaw's Text Classification Challenge - A Kaggle Competition(NYC)](https://nycdatascience.com/blog/student-works/toxic-comment-classification-challenge-a-kaggle-competition/)


> 20190318 v1 初稿

评审老师好：

本次提交为恶毒评论的 Proposal，因为 Proposal 模版是英文的，而项目模版的前面 I问题的定义、II分析、III方法 部分与 Proposal 模版比较一致，这里就将 Proposal 的内容直接写在了项目模版的 I、II、III 部分，请老师审阅。

- - -

[TOC]
 
# I. 问题的定义

## 项目概述

本部分描述了项目的总体的概念。包括问题涉及哪个领域、选择项目的出发点、有哪些数据。

- **项目的背景：**是对网络中的评论进行情感分析。掌握大众的情感趋势有很多价值，比如检测对于公司品牌的评价、对于知名人物的评价或者政府的渔情监控等。
- **项目的出发点：**对自然语言处理有兴趣，生活中也接触到了不少产品。比如 `Apple Siri` 、 `小米 小爱同学` 等等。而且目前 `Text Analytics` 也已经达到了技术成熟区，如这张 Gartner 的炒作周期图所示[^hype]:
*<center> $_{数据科学炒作周期图（来自Gartner）}$</center>*
![-c800](media/15531425411472/15533390924889.jpg)
- **项目的数据：**本项目中的数据是 `kaggle` 中一次恶毒语言分类测试，主要目标是对所提供的数据中的评论进行情感的分类：
    - 属于监督学习下的深度学习解决范畴
    - 提供了带标签的训练集、不带标签的测试集
    - 需要提交测试集的情感分析归类分析
        - 分为6类负面情感
        - 归类为多选
- **项目领域：**涉及自然语言处理领域的工作，调研了一下目前NLP的情况，总结如下：
    - NLP的wiki定义是：Natural language processing (NLP) is a subfield of computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human (natural) languages, in particular how to program computers to process and analyze large amounts of natural language data. [^NLP]
    - NLU的定义是（是NLP的其中一部分）：Natural-language understanding (NLU) or natural-language interpretation (NLI)[1] is a subtopic of natural-language processing in artificial intelligence that deals with machine reading comprehension. Natural-language understanding is considered an AI-hard problem. [^NLU]
    - 本项目中要实现的情感分析实际上是 `对话平台` 中的一部分[^con_archi]：
*<center> $ _{对话平台高阶架构（来自Gartner）}$ </center>* 
![mlnd_capestone1-c800](media/15531425411472/mlnd_capestone1.jpg)
    - 其中的情感分析 `Sentiment Analytics`，Gartner公司的定义是：Categorizes and identifies opinions expressed in the phrases the user is writing and attempts to derive the user’s attitude toward topics, products or services. 从图中可以看出，情感分析只是 Processing 中 Natural-Language Processing(NLP) 分析的一小环。而所有NLP输出后会进入到 Intent Maching 阶段，之后就会推给算法进行处理。再之后会根据场景需求作出反馈。完成 `输入处理-算法实现-输出生成` 对话平台的核心功能。
    - 实际工业化产品，可以参照 `Amazon Lex` 深度学习平台的这篇介绍，在工业化的过程中，很多产品功能已经打包为模块，并且全部基于云计算实现，使得任何一个小的企业都可以尽快使用相关的会话平台，示例结构图如下[^amazon_lex]：
*<center> $_{在 Amazon Connect 联络中心使用 Amazon Lex 聊天机器人进行自然对话（来自AWS）}$</center>*
![-c800](media/15531425411472/15534770958338.png)

[^hype]: [Hype Cycle for Data Science and Machine Learning, 2018（Gartner）](https://www.gartner.com/document/3883664?ref=solrAll&refval=218831438&qid=f09c9a3aa881a9d98e9e862)
[^NLP]: [Natural Language Processing（Wiki）](https://en.wikipedia.org/wiki/Natural_language_processing)
[^con_archi]: [Architecture of Conversational Platforms（Gartner）](https://www.gartner.com/document/3889098?ref=solrAll&refval=218829016&qid=c2ec3dd07deced1f309)
[^amazon_lex]: [Amazon Lex（AWS）](https://amazonaws-china.com/cn/lex/)
[^NLU]: [Natural Language Understanding（Wiki）](https://en.wikipedia.org/wiki/Natural-language_understanding)

## 问题陈述

本部分为项目解决问题将要使用的策略（任务的大纲）的讲解。明确想要期望的结果是怎样的。在本部分要明确定义解决的问题、和如何解决并且期望的结果是什么。

### // 要解决的问题

根据给出的 train 带标签数据，通过使用深度学习（监督学习）得出分类算法，能够对未来评论语句的负面情感进行感知。

### // 解决问题的方法

- I Prepare
    - 检查数据质量，如果需要做相应处理
    - 将 train 数据划分为 train 和 validation 两个集合
- II Algorithm
    - 根据项目的特点选择算法
    - 选择合适的迁移学习数据
    - 搭建算法学习环境
    - 得出模型
    - 得出算法结论
- III Optimize
    - 回顾模型和项目要求对算法进行优化调整
    - 搜索相关文献
    - 调整算法模型
    - 得出最终结论
- IV Finish
    - 完成论文的组织修改
    - 准备所有资源列表
    - 提交项目

## 评价指标
这部分包括用于评价自己的模型和结果的**指标**和**计算方法**。包括定义了所使用的指标和计算方法以及这些指标和计算方法的合理性。

- 数据来源于 Kaggle 竞赛，最终评价为上传 Kaggle 得出的评分。
- Kaggle 的评分方式为：
    - 根据 test 数据计算出 result
    - result 为 test 数据的多分类准确性测量
    - Kaggle 的评分标准并未公开

# II. 分析

## 数据的探索
在这一部分，你需要探索你将要使用的数据。数据可以是若干个数据集，或者输入数据/文件，甚至可以是一个设定环境。你需要详尽地描述数据的类型。如果可以的话，你需要展示数据的一些统计量和基本信息（例如输入的特征（features)，输入里与定义相关的特性，或者环境的描述）。你还要说明数据中的任何需要被关注的异常或有趣的性质（例如需要做变换的特征，离群值等等）。

## / 回答

- _如果你使用了数据集，你要详尽地讨论了你所使用数据集的某些特征，并且为阅读者呈现一个直观的样本_

**数据列说明：**
1. train数据包括 id + comment + 6categroy label，一共是8列数据。其中6个分类标签为多选分类（用1标识），同一条数据可以同时属于这6个分类（这样的例子有39个）。也可以那个都不属于（所有分类标识都为0）
1. test数据包括 id + comment 是用来测试的数据
1. test_label数据包括 id + 6category bilabel，提示了那条数据是恶毒数据（所有6分类都为1，反之全为0）

- _如果你使用了数据集，你要计算并描述了它们的统计量，并对其中与你问题相关的地方进行讨论_

**数据文件列表：**

| file | shape | note |
| --- | --- | --- |
| train.csv | 159571, 8 | 包含id、评论和分类 |
| test.csv | 153164, 2 | 包含id和评论 |
| test_labels.csv | 153164, 7 | 包含id和2分类 |

- _如果你**没有**使用数据集，你需要对你所使用的输入空间（input space)或输入数据进行讨论？_

1. 使用了数据集，Pass此部分。

- _数据集或输入中存在的异常，缺陷或其他特性是否得到了处理？(例如分类变数，缺失数据，离群值等）_

1. 所有数据都很干净，无重复，无缺失
2. 由于是语言分析，其他统计学参数相关度不大
3. 比较1:恶毒评论比率
	1. train数据0.1017，test数据0.3779
4. 思考：对于test数据有两种使用方法
	1. 第一种全部使用，生成结果以后可以对非恶毒评论是否正确做判断。但这个结果可能会诱导分析人员进行参数调优，违反测试数据只能使用一次的原则。
	2. 第二种情况，过滤出test中的恶毒评论进行分析，不考虑正常评论。这样可以不犯第一种的错误。
	3. 提交要求：根据 `Kaggle` 竞赛的说明和 `sample submition` 文件样式，需要提交包括非恶毒评论的分类[^kaggle_official]。
	4. 事后验证：但是可以根据 kaggle 提交的成绩和 test 中正常评论筛选出来的比率做比较，检查以下假设：是否恶毒评论分类越准确的算法，在识别正常评论方面也会很准确。
5. **请教问题：**请问老师这里应该怎么处理比较好，如果上面假设有关系的话，应该根据这种反馈调整算法得到更好分数么？为什么 Kaggle 在竞赛的 test 数据中会披露那些语句不是恶毒评论，这样做的目的是什么？

[^kaggle_official]: [Toxic Comment Classification Challenge(Kaggle)](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data)

## 探索性可视化
在这一部分，你需要对数据的特征或特性进行概括性或提取性的可视化。这个可视化的过程应该要适应你所使用的数据。就你为何使用这个形式的可视化，以及这个可视化过程为什么是有意义的，进行一定的讨论。

## / 回答

- _你是否对数据中与问题有关的特性进行了可视化？_
    - 恶毒评论单分类比例汇总，可以看到6个分类的排列情况：
![-c](media/15531425411472/15541790824802.jpg)
    - 多选分类出现的统计：因为这里是多选，想展示下多选的组合情况，因为从1个分类到6个分类的情况全部都有，没有想到用那个图。
    - **请问老师：**这种情况用什么可视化展示比较好？我想出的折中方法是做热力图，展示两两出现的feature的集合比率。但又觉得这样展示比较奇怪。
- _你对可视化结果进行详尽的分析和讨论了吗？_
    - 根据上面的分类情况，可以看到6个分类从 toxic、obscene、insult、severe toxic、identity hate、threat 逐渐比例下降。而情感的极端情况也是逐渐增加，和假设的情况比较温和。
- _绘图的坐标轴，标题，基准面是不是清晰定义了？_
    - 将在后续版本中完成。
- **---v1 updata---**
    - 根据评审老师提醒，这里还应该对数据的特点进行描述：
        - 这是一个不平衡分类数据。
        - 这是一个多分类数据。

### 算法和技术
在这一部分，你需要讨论你解决问题时用到的算法和技术。你需要根据问题的特性和所属领域来论述使用这些方法的合理性。你需要考虑：
- _你所使用的算法，包括用到的变量/参数都清晰地说明了吗？_
- _你是否已经详尽地描述并讨论了使用这些技术的合理性？_
- _你是否清晰地描述了这些算法和技术具体会如何处理这些数据？_

### / 使用的算法和技术

根据项目要求，分为3个相并列算法部分完成：
1. 连续词袋模型。
2. wrod2vex + GloVe（6B）模型。
3. word2vex + GloVe（840B）模型。

**连续词袋模型：**
- 环境准备
    - 从文件生成数据 `train_features`,`train_target`, `test`, `test_labels`。
    - 最后的提交为 `submission.csv` 对应为根据算法生成的 `test` 多分类概率。
    - `test_labels`标识了是否为普通或者属于至少一个分类的test属性，在本方法中不采用。
- 向量化
    - 使用 `TfidfVectorzer` 将 comment 数据进行向量化。
        - comment 向量化（word）
            - 对 comment 进行以词为单位的向量化，使用参数 `analyzer='word' ngram_range=(1,1)`
            - 得出 1w dimension
            - 存为 `train_comment_features`, `test_comment_features`
        - ngram 向量化（character）
            - 对 comment 进行以字母（2-4个）为单位的向量化，使用参数 `analyzer='char' ngram_range=(2,4)`
            - 得出 5w dimension
            - 存为 `train_character_features`, `test_character_features` 
    - 将上述两个向量化堆叠
            - 存为`train_features`, `test_features`
            - 都具有 6w demension
- 评分
    - 建立评分规则
        - 设定空 `score_list`
        - 根据提交要求设定 `submission` 格式
        - 定义 classifier 使用 `LogisticRegression`
    - 循环评分
        - 对6个分类（列）使用循环完成评分
        - 使用 `train_features`, `train_target` 对模型进行适配
        - 使用模型计算 score
        - 将 score 续写到 score_list 并打印 score
    - 平均评分
        - 对6个分类的评分做平均，得出最终评分（训练数据集的）
- 结论
    - 使用训练好的算法得出 submission.csv
    - 提交 kaggle 计算得分

**wrod2vex 模型（keras + Glove（6B tokens, 400K vocab）:**
- 环境准备
    - 从文件生成数据 `train_features`,`train_target`, `test`, `test_labels`。
    - 最后的提交为 `submission.csv` 对应为根据算法生成的 `test` 多分类概率。
    - `test_labels`标识了是否为普通或者属于至少一个分类的test属性，在本方法中不采用。
- Embedding Layer 准备
    - 上传 Embedding Layer 文件。
    - 准备 Embedding Layer 层。
        - 设定 input_dim 参数
        - 设定 output_dim 参数
        - 设定 input_length 参数
    - 将上述两个向量化堆叠
            - 存为`train_features`, `test_features`
            - 都具有 6w demension
- 卷基层建立（1D）
    - 建立 embedded_sequences
    - 建立 activation（n次）
    - 建立 Flatten
    - 建立 Dense
- 评分
    - 使用 mode.evalute进行评分（training）
- 结论
    - 使用训练好的算法得出 submission.csv
    - 提交 kaggle 计算得分

**wrod2vex 模型（keras + Glove（840B tokens, 2.2M vocab）:**
- 基本同上个模型，通过对比 6B 和 840B 的 Pre-Trained 数据，发现数据对于模型训练的影响。

完成项目资源说明：
1. 因为时间比较紧凑，开始想使用优达深度学习的项目空间（前一个项目还剩比较多GPU时间），结果项目介绍中的3个词处理平台都需要进行命令行操作需要使用 AWS 空间带 GPU 的虚拟机解决[^awsdl]。
2. 后来在探索中发现 Google Colab 提供在线 Jupyter Notebook 可以免费集成 GPU/TPU，学习成本更好，改为尝试 Colab[^colab]。
3. 库方面开始像使用课程中讲解的 keras，感觉比较简洁。后续探索发现很多介绍使用的是 Gemsim，原因是 Gesim 底层使用的 C ，效率很快，但需要 Cpython 支持[^gensim]。
4. 具体方法将在项目代码部分做详细说明。

[^colab]: [Learn how to build deep learning systems in Google Colaboratory](https://adventuresinmachinelearning.com/introduction-to-google-colaboratory/)
[^awsdl]: [How to create a TensorFlow deep learning powerhouse on Amazon AWS](https://adventuresinmachinelearning.com/category/amazon-aws/)
[^gensim]: [Gensim Wrod2Vec Tutorial(Web)](https://adventuresinmachinelearning.com/gensim-word2vec-tutorial/)
[^glove]: [GloVe: Global Vectors for Word Representation（Stanford）](https://nlp.stanford.edu/projects/glove/)
[^vector]: [English word vectors（FastText）](https://fasttext.cc/docs/en/english-vectors.html)
[^udadl]: [Udacity Deep Learning Workspace (Udacity)](https://classroom.udacity.com/nanodegrees/nd009-cn-advanced/parts/bfc08027-d9e2-4483-839c-e6ec1e2ada4c/modules/10b781e7-357b-4e54-8180-4a55a1daf6dc/lessons/2df3b94c-4f09-476a-8397-e8841b147f84/concepts/e4af01b5-73c7-4af7-ba56-e0098bd0b026)
[^glovevec]: [How is GloVe different from word2vec](https://www.quora.com/How-is-GloVe-different-from-word2vec)
[^subword]: [FastText Word Embedding](https://cloud.tencent.com/developer/news/297583)

### / 论述技术的合理性

本节主要论述使用 wrod2vex 的工作原理：

**word2vex之前的算法：**
在word2vex之前的几种方法简介：
- Word Embedding ： 是将自然语言中的组语言模型（language modeling）映射到特征学习技术（feature learning techniques）的方法。输入是自然语言，输出是把输入中的单词（或者短语）映射成向量（转化为数学问题）。
- Word Embedding 方法1：BOG（词袋，或者CBOG），方法是将输入中出现的所有词作独热编码，对于这些采用独热编码的向量，在句子的颗粒度作加和。这种方法的缺点有两个：
    - 没有考虑单词顺序（相邻关系）的影响。
    - 向量可能非常长。
- Word Embedding 方法2：n-gram ，这种方法假设，每一个词出现的概率仅依赖于该词前面的n-1个词。
- Word Embedding 方法3：Cocurrence Matrix（共现矩阵），这种方法通过限定窗口大小来看核心词和窗口（类似于n-gram中的n）中其他词的向量关系。
    - 比如窗口为2的例子如下：
![-c400](media/15531425411472/15547850695559.jpg)
    - 最后得出矩阵：
![-c400](media/15531425411472/15547851371819.jpg)
- Word Embedding 方法4：NLM（神经语言模型，NNLM）。使用词向量作输入，NLM 要解决的问题是解析出相似含义词都有哪些，并且让相近含义的词在目标向量空间中距离更近。

**word2vex原理：**
在前面的`NLM`基础上扩展的的`word2vex`的核心思想是将一个词的意义用它周围的词进行表示（In Word2Vec, the meaning of a word is roughly translatable to context – and it basically works [^word2vectu].） ，这种表示是将他周围的词做为目标词的预测，转换为向量。这种向量对应的是词语的意义，这样多对一的关系，可以简化计算，也更准确。所以方法叫做 word2vec，比如这个奖1万个词映射到300维意义的示例图，出处同本段脚注：

![-c600](media/15550243107913/15554707517198.jpg)

- 1万个output是过程数据，用于计算过程中的反向传播。
- 最终的输出是 10000 * 300 的矩阵。
- 当有一个词的时候，我们就可以查这 10000 个词的表，得出这个词是在 300 个向量中，最符合（概率最大）的，就预测词的意思了。
- 但是1万个input计算量比较复杂，所以还使用了 negative sampling 的方法进行了简化计算。比如这个 `vocabulary_size = 7`, `embedding_size=3` 的例子[^word2veckeras]：

![-c200](media/15550243107913/15554778486024.jpg)


[^word2vectu]: [Python gensim Word2Vec tutorial with TensorFlow and Keras](https://adventuresinmachinelearning.com/gensim-word2vec-tutorial/)
[^word2veckeras]: [A Word2Vec Keras tutorial](https://adventuresinmachinelearning.com/word2vec-keras-tutorial/)

word2vex具体计算采用了两种可选的数学计算方法：CBOW 和 Skip-gram的方式，再加上 Hierarchical Softmax 进行降维降低计算成本。两种方式的主要区别是（参考前面窗口大小的概念）：
- CBOW 是根据周围的词预测核心词（Condition on context, and generate centre word）：
![-c400](media/15531425411472/15547859277433.jpg)
- Skip-gram 是根据核心词预测周围的词（Generates each word in context given centre word）：
![-c400](media/15531425411472/15547859873217.jpg)

**迁移学习数据选择：**
- 选择 gensim 直接实现 word2vex，原因是：  
- 也可以选择 fastText [^fasttest] 。在 word2vex 的基础上增加了词频的相关数据，由 facebook 提出。比如这个数据：FastText `Common Crawl 2M with Subword 版本（5.83GB）`[^vector]。
    - WordVector 的调用方式见脚注链接说明。
    - WordVector 支持157种语言，包括中文，同见脚注链接。
    - Subword 是对词频出现较少词的修正：
        - 因为 word2vec 使用的最小单位是一个word，通过中心词预测上下文的词汇。
        - 那么，一个句子长短不同，我们怎么衡量词之间的向量关系呢？我们可以使用 n-gram 限定一次考察几个词的关系。        
        - 比如 n-gram = 3，前2个词是 featrue，后面的一个词就是 label。
        - 具体计算时候，还会设定一些常用的词不使用 n-gram[^subword]。
- 也可以选择GloVe `Common Crawl 840B 版本（2.03GB）`[^glove]。GloVe 的主要特点是结合了统计值和向量（距离），而 WordVector 只考虑向量 [^glovevec]。

**参考资料：**
1. fastText官网[^fasttest]
2. Word Embedding 与 Word2Vec[^embedding1]
3. 自然语言处理 Word Embedding[^embedding2]
4. 图解 Word2Vec[^embedding2]

[^fasttest]: [fastText官网（fastText）](https://fasttext.cc/)
[^embedding1]: [Word Embedding 与 Word2Vec（csdn）](https://blog.csdn.net/baimafujinji/article/details/77836142)
[^embedding2]: [自然语言处理 Word Embedding（csdn）](https://blog.csdn.net/L_R_H000/article/details/81320286)
[^embedding3]: [图解 Word2Vec（wechat）](https://mp.weixin.qq.com/s/CgbmO6u-Kk-2fCF4ZwtcZQ)

### / 使用算法处理数据的过程

### 基准模型
在这一部分，你需要提供一个可以用于衡量解决方案性能的基准结果/阈值。这个基准模型要能够和你的解决方案的性能进行比较。你也应该讨论你为什么使用这个基准模型。一些需要考虑的问题：
- _你是否提供了作为基准的结果或数值，它们能够衡量模型的性能吗？_
- _该基准是如何得到的（是靠数据还是假设）？_

### / 基准值和衡量标准

衡量标准为 Kaggle 的竞赛标准，当提交数据之后，Kaggle 将会在后台与 Testing 的标签（并未发布）作比较，得出评分。
**---updated v2---：**
使用的是 AUC 进行衡量标准，AUC 可以衡量分类问题的效率，具体原理下面介绍。

### / 基准值有效的原理

由于是基于 Label 的评分，为最终依据，并且后续不会有更新。属于监督学习的范围，评分有效性高且为唯一评分标准。
**---updated v2---：**
对 AUC 的解释：
- 混淆矩阵
    - 混淆矩阵是通过衡量 False Positive 和 Ture Positive 的比率来评判模型的效率的。
    - 这两个指标的定义见混淆矩阵图：
![-c](media/15550243107913/15552313035152.jpg)

- 受试者工作曲线（ROC Curve）
    - 根据不同的数据分割，我们可以得到很多 （[0,1],[0,1]) 的二维坐标，这些坐标连接起来就构成了 ROC Curve： 
![-c400](media/15550243107913/15552322447513.jpg)

- 曲线面积 （AUC）
    - 那么仅仅比较不同算法之间的曲线关系，有时候不是很明显[^auc]：
![-c300](media/15550243107913/15552323297557.jpg)
    - 可以使用曲线下的面积进行衡量（ AUC ： Area Under Curve）[^roc_and_auc]，具体计算公式见[^auc_standfor]：
![-c400](media/15550243107913/15552323916924.jpg)

[^roc_and_auc]: [Understanding the ROC and the AUC Curve](https://towardsdatascience.com/understanding-the-roc-and-auc-curves-a05b68550b69)
[^auc]: [Konw about AUC](http://fastml.com/what-you-wanted-to-know-about-auc/)
[^auc_standfor]: [What does AUC stand for and what is it(StackExchange)](https://stats.stackexchange.com/questions/132777/what-does-auc-stand-for-and-what-is-it)

## III. 方法

### 数据预处理
在这一部分， 你需要清晰记录你所有必要的数据预处理步骤。在前一个部分所描述的数据的异常或特性在这一部分需要被更正和处理。需要考虑的问题有：
- _如果你选择的算法需要进行特征选取或特征变换，你对此进行记录和描述了吗？_
- _**数据的探索**这一部分中提及的异常和特性是否被更正了，对此进行记录和描述了吗？_
- _如果你认为不需要进行预处理，你解释个中原因了吗？_

### 执行过程
在这一部分， 你需要描述你所建立的模型在给定数据上执行过程。模型的执行过程，以及过程中遇到的困难的描述应该清晰明了地记录和描述。需要考虑的问题：
- _你所用到的算法和技术执行的方式是否清晰记录了？_
- _在运用上面所提及的技术及指标的执行过程中是否遇到了困难，是否需要作出改动来得到想要的结果？_
- _是否有需要记录解释的代码片段(例如复杂的函数）？_

### 完善
在这一部分，你需要描述你对原有的算法和技术完善的过程。例如调整模型的参数以达到更好的结果的过程应该有所记录。你需要记录最初和最终的模型，以及过程中有代表性意义的结果。你需要考虑的问题：
- _初始结果是否清晰记录了？_
- _完善的过程是否清晰记录了，其中使用了什么技术？_
- _完善过程中的结果以及最终结果是否清晰记录了？_


## IV. 结果

### 模型的评价与验证
在这一部分，你需要对你得出的最终模型的各种技术质量进行详尽的评价。最终模型是怎么得出来的，为什么它会被选为最佳需要清晰地描述。你也需要对模型和结果可靠性作出验证分析，譬如对输入数据或环境的一些操控是否会对结果产生影响（敏感性分析sensitivity analysis）。一些需要考虑的问题：
- _最终的模型是否合理，跟期待的结果是否一致？最后的各种参数是否合理？_
- _模型是否对于这个问题是否足够稳健可靠？训练数据或输入的一些微小的改变是否会极大影响结果？（鲁棒性）_
- _这个模型得出的结果是否可信？_

### 合理性分析
在这个部分，你需要利用一些统计分析，把你的最终模型得到的结果与你的前面设定的基准模型进行对比。你也分析你的最终模型和结果是否确确实实解决了你在这个项目里设定的问题。你需要考虑：
- _最终结果对比你的基准模型表现得更好还是有所逊色？_
- _你是否详尽地分析和讨论了最终结果？_
- _最终结果是不是确确实实解决了问题？_


## V. 项目结论
_（大概 1-2 页）_

### 结果可视化
在这一部分，你需要用可视化的方式展示项目中需要强调的重要技术特性。至于什么形式，你可以自由把握，但需要表达出一个关于这个项目重要的结论和特点，并对此作出讨论。一些需要考虑的：
- _你是否对一个与问题，数据集，输入数据，或结果相关的，重要的技术特性进行了可视化？_
- _可视化结果是否详尽的分析讨论了？_
- _绘图的坐标轴，标题，基准面是不是清晰定义了？_


### 对项目的思考
在这一部分，你需要从头到尾总结一下整个问题的解决方案，讨论其中你认为有趣或困难的地方。从整体来反思一下整个项目，确保自己对整个流程是明确掌握的。需要考虑：
- _你是否详尽总结了项目的整个流程？_
- _项目里有哪些比较有意思的地方？_
- _项目里有哪些比较困难的地方？_
- _最终模型和结果是否符合你对这个问题的期望？它可以在通用的场景下解决这些类型的问题吗？_


### 需要作出的改进
在这一部分，你需要讨论你可以怎么样去完善你执行流程中的某一方面。例如考虑一下你的操作的方法是否可以进一步推广，泛化，有没有需要作出变更的地方。你并不需要确实作出这些改进，不过你应能够讨论这些改进可能对结果的影响，并与现有结果进行比较。一些需要考虑的问题：
- _是否可以有算法和技术层面的进一步的完善？_
- _是否有一些你了解到，但是你还没能够实践的算法和技术？_
- _如果将你最终模型作为新的基准，你认为还能有更好的解决方案吗？_

----------

**在提交之前， 问一下自己：** 

- 你所写的项目报告结构对比于这个模板而言足够清晰了没有？
- 每一个部分（尤其**分析**和**方法**）是否清晰，简洁，明了？有没有存在歧义的术语和用语需要进一步说明的？
- 你的目标读者是不是能够明白你的分析，方法和结果？
- 报告里面是否有语法错误或拼写错误？
- 报告里提到的一些外部资料及来源是不是都正确引述或引用了？
- 代码可读性是否良好？必要的注释是否加上了？
- 代码是否可以顺利运行并重现跟报告相似的结果？

> 脚注：