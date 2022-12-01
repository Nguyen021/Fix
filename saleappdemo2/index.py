from flask import render_template, request
from saleappdemo2 import app, admin
import dao


@app.route('/')
def home():
    cate_id = request.args.get('category_id')
    kw = request.args.get('keyword')
    p = dao.load_product(category_id=cate_id, kw=kw)
    return render_template('index.html',
                           products=p)


@app.context_processor
def common():
    cate = dao.load_category()
    return {
        'categories': cate
    }


if __name__ == '__main__':
    from saleappdemo2 import admin
    app.run(debug=True, port=2001)
