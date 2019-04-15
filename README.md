# Project 1 Specification
____________
### Groups Members
* Alexandre Geraldo
* Austin Brantley
* Franklin Gonzales
* Prashanth Saseenthar
  
 ### Analytics Paradigm Guide
1. Decompose the Ask
2. Identity Data Sources
3. Define Strategy and Metrics
4. Build Data Retrieval Plan
5. Retrieve the Data
6. Assemlble and Clean
7. Analyze for Trends
8. Acknowledge Limitations
9. Make the Call or Tell the Story

### Project Scope
_____
#### Initial discussion
- How to make money as a Youtuber ?
- Quote from Homework#1: 
  - Many organizations spend months looking through past projects in an attempt to discover some trick to finding success.You will organize and analyze a database of four thousand past projects in order to uncover any hidden trends.
- Project template:
  - Our project is to uncover patterns in criminal activity around Los Angeles. We'll examine relationships between types of crime and location; crime rates and times of day; trends in crime rates over the course of the year; and related questions, as the data admits.
- Trying to be more specific with the scope:
  - Youtube traffic is the kind of traffic you can’t ignore. In other words, by harnessing the power of YouTube, you can increase your **brand’s visibility exponentially**.So learning the techniques for getting a video to rank well on YouTube is of prime importance.
- Draft scope:
  - Finding success in launching a marketing campaign for a product using social media such as Youtube.

#### Scope(needs to be approved by BCS & Group Members)
**Question :** How to increase a product brand's visibility using Social Media ? 

- How to increase visibility ?
  - Marketing campaings on TV, Internet, Radio, etc.
- How to build product popularity ?
  - By creating an identity with our consumers.
- Who are your customers ?
  - Based on the company's product brand.
- Where are the customers ?
  - Worldwide
- What would be a good prove of concept (POC)?
  - By using Social Media platforms such as YouTube.
- Why YouTube ?
  - It has a wide reach and generates plenty of traffic.
  - YouTube has over 1 billion users, who spend millions of hours per day viewing videos.
  - YouTube is localized in over 70 countries and is available in 76 languages.
  - It has greater reach than cable in the US.
  - It’s huge on mobile – more than 50% of YouTube views are via mobile phones.
  - The earning potential is enormous. Recent statistics show that every year, there’s been a 50% increase in the channels earning 6 figures annually.
  - It’s a social network.
  - It’s a search engine.
  - Pay Per (Actual) View Of Your Ad.
- Facts:
    - Increasing the number of video views, likes and comments can lead to a product visibility increase in an exponential rate.
    - Learning and using previous good experiences in social networks of other players can lead to a successful marketing campaign. 
- Why trend is so important ?
  - Trending helps viewers see what's happening on YouTube and in the world. Some trends are predictable, like a new song from a popular artist or a new movie trailer. Others are surprising, like a viral video. Trending aims to surface videos that a wide range of viewers will appreciate.

- What strategies did fastest growing brands use. 
  -Who are they? (data on viewer/sub/likes growth)
  -What is the desired length of the videos?
  -tags related to higher views. which tags to avoid?
  -timing of publishing. Time of day and season(quarters)
  
  


#### Strategic
- Use YouTube trend dataset for:
  - Uncover hidden trends of videos and channels.
  - Understand how trending and ranking algorithms works.
- Build a second dataset based on YouTube dataset for:
  - Provide additional data for the current dataset such as videos length. Video length is used on the ranking algorithm.
  - Identity videos and/or channels that can be considered outliers (monetization).
  
#### Plan (**Analytics Paradigm**)
2. Identity Data Sources
    - Kaggle
      - https://www.kaggle.com/datasnaek/youtube-new
    - API
      - https://developers.google.com/youtube/v3/
    - Web Scraping
      - https://socialblade.com/youtube/

    - Sentiment Analysis
      - https://www.nltk.org/

3. Define Strategy and Metrics
   + Discover the trends of the success for channels and videos.
   + Top trending videos -> top channels -> hidden trends -> marketing model.
   + Videos and channels can demostrate trends
   + Channels data can be boosted using additional datasources.
   + Evaluate the channel performance against actual data (identity outiers).
 
 ### Correlations
* Views and Likes
* Views and Comments
* Likes and Comments
* Views and Video Lenght
* Likes, Video Lenght, Views (BubbleChart)
* Numbers of Trending Days x Countries
* Video Title lenght and Views
* Video Tags and Views
* Numbers of Comments x Trending Days
* Raking and Views

### Trends
* Number of Views per trending videos
* Channels with largest number of trending videos
* Video category with largest number of trending videos
* Video Lenght Distribution
* Publishing Days / Hours
* Compare Total subscriber count, daily subscriber count, total view count, and daily view count
* Common words used in videos titles (WordClouds)
* Common words used in videos tags (WordClouds)
* Top Videos Visual Wall (Thumbnails)
* Ratio of Like/Dislikes of the channels
* Ranking
  * **Most used tags keywords**
  * **Most used video title keywords**

### Time Series
* Trends videos over time
* Total of publish videos over time

### Possible Questions to Investigate:
* What tags appear in the greatest number of videos? What tags seem to draw in more views, likes, and comments?
* Which categories are most popular? Which categories draw engagement in the form of likes, views, and comments?


