from flask import Flask, jsonify, request, render_template, Response
import pandas as pd
from scrape_mars import scrape
import pymongo


app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/api/consigue")
def consigue():
    results_dict=scrape()

    conn='mongodb://localhost:27017'
    client=pymongo.MongoClient(conn)
    db=client['mars_db']
    collection=db['scraped']
    collection.delete_many({})
    collection.insert_one(results_dict)

    resultado = list(collection.find({}))
    resultado=resultado[0]
    resultado={
        'news':resultado['news'],
        'feat_img':resultado['feat_img'],
        'weather':resultado['weather'],
        'html_table':resultado['html_table'],
        'hemisphere':resultado['hemisphere_img'],
    }
    return resultado
    #return results_dict
    
if __name__=='__main__':
    app.run()