{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "22134e22",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>v1</th>\n",
       "      <th>v2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ham</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ham</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>spam</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ham</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ham</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5567</th>\n",
       "      <td>spam</td>\n",
       "      <td>This is the 2nd time we have tried 2 contact u...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5568</th>\n",
       "      <td>ham</td>\n",
       "      <td>Will Ì_ b going to esplanade fr home?</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5569</th>\n",
       "      <td>ham</td>\n",
       "      <td>Pity, * was in mood for that. So...any other s...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5570</th>\n",
       "      <td>ham</td>\n",
       "      <td>The guy did some bitching but I acted like i'd...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5571</th>\n",
       "      <td>ham</td>\n",
       "      <td>Rofl. Its true to its name</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5572 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        v1                                                 v2\n",
       "0      ham  Go until jurong point, crazy.. Available only ...\n",
       "1      ham                      Ok lar... Joking wif u oni...\n",
       "2     spam  Free entry in 2 a wkly comp to win FA Cup fina...\n",
       "3      ham  U dun say so early hor... U c already then say...\n",
       "4      ham  Nah I don't think he goes to usf, he lives aro...\n",
       "...    ...                                                ...\n",
       "5567  spam  This is the 2nd time we have tried 2 contact u...\n",
       "5568   ham              Will Ì_ b going to esplanade fr home?\n",
       "5569   ham  Pity, * was in mood for that. So...any other s...\n",
       "5570   ham  The guy did some bitching but I acted like i'd...\n",
       "5571   ham                         Rofl. Its true to its name\n",
       "\n",
       "[5572 rows x 2 columns]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "data=pd.read_csv('spam.csv',encoding='latin-1')\n",
    "df=pd.DataFrame(data,columns=['v1','v2'])\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "beb89f82",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>v1</th>\n",
       "      <th>v2</th>\n",
       "      <th>v3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ham</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ham</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>spam</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ham</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ham</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5567</th>\n",
       "      <td>spam</td>\n",
       "      <td>This is the 2nd time we have tried 2 contact u...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5568</th>\n",
       "      <td>ham</td>\n",
       "      <td>Will Ì_ b going to esplanade fr home?</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5569</th>\n",
       "      <td>ham</td>\n",
       "      <td>Pity, * was in mood for that. So...any other s...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5570</th>\n",
       "      <td>ham</td>\n",
       "      <td>The guy did some bitching but I acted like i'd...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5571</th>\n",
       "      <td>ham</td>\n",
       "      <td>Rofl. Its true to its name</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5572 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        v1                                                 v2  v3\n",
       "0      ham  Go until jurong point, crazy.. Available only ...   1\n",
       "1      ham                      Ok lar... Joking wif u oni...   1\n",
       "2     spam  Free entry in 2 a wkly comp to win FA Cup fina...   0\n",
       "3      ham  U dun say so early hor... U c already then say...   1\n",
       "4      ham  Nah I don't think he goes to usf, he lives aro...   1\n",
       "...    ...                                                ...  ..\n",
       "5567  spam  This is the 2nd time we have tried 2 contact u...   0\n",
       "5568   ham              Will Ì_ b going to esplanade fr home?   1\n",
       "5569   ham  Pity, * was in mood for that. So...any other s...   1\n",
       "5570   ham  The guy did some bitching but I acted like i'd...   1\n",
       "5571   ham                         Rofl. Its true to its name   1\n",
       "\n",
       "[5572 rows x 3 columns]"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['v3']=df['v1'].apply(lambda x:1 if x=='ham' else 0)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "7f5ece03",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(5572, 8672)\n",
      "(5572,)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "cv=CountVectorizer()\n",
    "x=cv.fit_transform(df['v2']).toarray()\n",
    "y=df['v3']\n",
    "print(x.shape)\n",
    "print(y.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "2ddb22b3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-7 {color: black;background-color: white;}#sk-container-id-7 pre{padding: 0;}#sk-container-id-7 div.sk-toggleable {background-color: white;}#sk-container-id-7 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-7 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-7 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-7 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-7 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-7 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-7 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-7 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-7 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-7 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-7 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-7 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-7 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-7 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-7 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-7 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-7 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-7 div.sk-item {position: relative;z-index: 1;}#sk-container-id-7 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-7 div.sk-item::before, #sk-container-id-7 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-7 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-7 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-7 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-7 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-7 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-7 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-7 div.sk-label-container {text-align: center;}#sk-container-id-7 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-7 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-7\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>DecisionTreeClassifier()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-7\" type=\"checkbox\" checked><label for=\"sk-estimator-id-7\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">DecisionTreeClassifier</label><div class=\"sk-toggleable__content\"><pre>DecisionTreeClassifier()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "DecisionTreeClassifier()"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "svc=DecisionTreeClassifier()\n",
    "model=svc.fit(x_train,y_train)\n",
    "model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "ef1994f5",
   "metadata": {},
   "outputs": [],
   "source": [
    "prediction=model.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "e692b405",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9713004484304932"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test,prediction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "4c6e602c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hi team, just a reminder that we have our project update meeting tomorrow at 10 AM. Please be prepared with your progress reports.\n",
      "Predictions: [1]\n"
     ]
    }
   ],
   "source": [
    "new_emails = [input()]\n",
    "new_emails_vectorized = cv.transform(new_emails).toarray()\n",
    "predictions = model.predict(new_emails_vectorized)\n",
    "print(\"Predictions:\", predictions)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "6ba2d8c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Predictions: [0 1]\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ff77dea",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
