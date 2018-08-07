from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(article_topic , article_title , article_rating):
	article_object = Knowledge(
		article_topic=article_topic,
		article_title=article_title,
		article_rate=article_rating)
	session.add(article_object)
	session.commit()

def query_all_articles():
	knowledge = session.query(
		Knowledge).all()
	return knowledge


def query_article_by_topic(article_topic):
	article_by_topic = session.query(
		Knowledge).filter_by(
		article_topic=article_topic).all()
	return article_by_topic


def delete_article_by_topic(article_topic):
		session.query(Knowledge).filter_by(
			article_topic=article_topic).delete()
		session.commit()

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()


def edit_article_rating():
	pass

def edit_rating(title , updated_rating):
	article = session.query(Knowledge).filter_by(
		article_title=title).all()
	for x in article:
		x.article_rate=updated_rating
		session.commit()

def delete_article_by_rating(threshold):
	art_rate=session.query(Knowledge).all()
	for x in art_rate:
		if x.article_rate<threshold:
			x.delete()
	session.commit()

#add_article("art1" , "title1" , "6")
#add_article("art1." , "title1" , "7")
#add_article("art2" , "title1" , "8")
#add_article("art3" , "title2" , "9")
#add_article("art4" , "title3" , "10")
#add_article("art5" , "title4" , "6")
#delete_all_articles()
#edit_rating("title1" , 10)
delete_article_by_rating(10)
print(query_all_articles())
#edit_rating("title1" , 10)

