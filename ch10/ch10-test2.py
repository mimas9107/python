# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 08:01:23 2024

@author: user
"""
import wordcloud

sample={'Hello':99, 'world':73, 'doraemon':63,'nobi':48}

show=wordcloud.WordCloud(background_color='white',width=200,height=200,margin=2)

show.fit_words(sample)
show.to_file('ch10-test2.png')