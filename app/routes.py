from PoGoInfo import PoGoInfo

@PoGoInfo.route('/')
@PoGoInfo.route('/inded')

def index():
    return "Hello World!"