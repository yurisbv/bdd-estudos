from vibora import Vibora
from vibora.responses import JsonResponse

app = Vibora()


@app.route('/')
async def home():
    data = ({"message":"Hello World"})
    return JsonResponse(data)


if __name__ == '__main__':
    app.run(debug=True)