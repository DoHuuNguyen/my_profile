from flask import Flask, render_template

app = Flask(__name__)

#Dữ liệu cá nhân và project
profile = {
    "name": "Đỗ Hữu Nguyện",
    "job":"Web Developer",
    "description":"Tôi yêu thích việc khám phá và phát triển bản thân, đam mê sáng tạo và học hỏi những cái mới",
    "email":"dohuunguyen2003ss@gmail.com",
    "github":"https://github.com/dohuunguyen2003",
}

projects = [
    {"title":"Website Bán Hàng","Link":"https://shoppe.com","desc":"Trang web bán đủ thứ"},
]
skills = [
    {"name": "Python", "level": 90},
    {"name": "HTML/CSS", "level": 85},
    {"name": "JavaScript", "level": 80},
    {"name": "Flask", "level": 75},
    {"name": "SQL", "level": 70}
]

@app.route("/")
def home():
    return render_template("index.html", profile=profile, projects=projects, skills=skills)
if __name__ == "__main__":
    app.run(debug=True)
    