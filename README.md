# Sentiment analysis of Social Media Posts 
The number of online trolls and bigots is rapidly increasing. This is because the user's anonymity has increased. They make comments and posts on social media accounts because they are confident that they will not be discovered. We designed a novel framework (named Pegasus) using SVM to prevent such nuisances. At first, it takes a username and a comment from the user. Based on the newly entered comment, it uses a pre-trained SVM model to tell whether the comment is racist or not. The speciality of the presented framework is that it can take comments on any language and classify it. For this, we used Google Translate API to translate any languages to English. Consecutively, the entered username is to check if the past few comments of the user are hateful or not. All the comments are again passed through the same SVM model as described above and a ratio is calculated. If the user has a higher ratio of hateful posts, then such a user can be a potential threat to the society and we can use this information to restrict that user from social media networks.
