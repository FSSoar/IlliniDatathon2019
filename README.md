# IlliniDatathon2019
Hello! Thanks for checking out our solution the Illini Datathon. As a jump start, if you would like to look at the NLP / Random Forest part of our solution, please see the Jupyter Notebook titled *[Final] NLP+RandomForest.ipynb*. The code is extremely long, because it combines much of the individual work done in the notebooks inside of the folder oldJupyter. Read the comments in each kernel to get a gist of what each kernel does, but the meat of the analysis and results are near the bottom, so head there. Otherwise, if you would like to look at the Keras and Sklearn LSTM, see the *Easy_LSTM* folder. This contains our long-term prediction model.

**IMPORTANT NOTE**: In our presentation, we discuss how the LSTM, Random Forest, and NLP can be combined. However, as of now, only the Random Forest and NLP are in sync. We used the Google News API for obtaining articles to run our NLP classifiers on, but there is an unfortunate restriction that a free user can only pull articles from up to one month ago. As a result, the NLP training (and consequently the main Random Forest model) could only use 2019 data, as that was the only data available. Because these were NOT used in the main LSTM function, our submitted values still follow competition rules.

### Working Code: 
- [Random Forest and NLP](https://github.com/FSSoar/IlliniDatathon2019/blob/master/%5BFinal%5D%20NLP%2BRandomForest.ipynb)
   - In order to run older Jupyter Notebooks them must be in the same directory as the FastAI Library. But the one linked above should be fine. 
- [LSTM](https://github.com/FSSoar/IlliniDatathon2019/blob/master/EasyLSTM/easyLSTMScript.py)

### Presentation: 
- [Presentation](https://github.com/FSSoar/IlliniDatathon2019/blob/master/Team%2012%20Datathon%20Presentation.pptx)


### APIs and Libraries Used
- AlphaVantage.co (Stock Information) 
- Google News (NLP)
- Keras
- Sklearn
- Textblob
- NLTK
- fastai
