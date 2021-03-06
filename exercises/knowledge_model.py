from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ ='knowledge'
	article_id=Column(Integer , primary_key=True)
	article_topic=Column(String)
	article_title=Column(String)
	article_rate=Column(Integer)

	def __repr__(self):
		if self.article_rate<7:
			return("Unfortunately, this article does not have a better rating. Maybe, this is an article that should be replaced soon!.")
		return ("If you want to learn about: {} , "
		"you should look at the Wikipedia article called :  {} , \n" 
		"We gave this article a rating of {} out of 10! \n"
		"article_id={}").format(
		self.article_topic,
		self.article_title,
		self.article_rate,
		self.article_id
		)


	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

	