import functions_framework
from kh2rando.seed_gen import generator

@functions_framework.http
def kh2_rando_seedgen(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'preset' in request_json:
        preset = request_json['preset']
    elif request_args and 'preset' in request_args:
        preset = request_args['preset']
    else:
        preset = 'League Summer 2025'
    
    # TODO: Add some error handling here
    seed_info = generator.make_random_seed_from_preset_name(preset)
    return seed_info.generator_string
