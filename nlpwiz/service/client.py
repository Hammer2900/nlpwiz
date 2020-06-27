
from nameko.standalone.rpc import ClusterRpcProxy

config = {
    'AMQP_URI': "amqp://guest:guest@127.0.0.1:5672"  # e.g. "pyamqp://guest:guest@localhost"
}


def invoke(model_name, method_name, params, model_params={}):
    with ClusterRpcProxy(config) as cluster_rpc:
        return cluster_rpc.model_service.invoke(model_name, method_name=method_name, params=params, model_params=model_params)

def infer(model_name, params, model_params={}):
    with ClusterRpcProxy(config) as cluster_rpc:
        return cluster_rpc.model_service.infer(model_name, params=params, model_params=model_params)

def model_test(model_name, *args, **kwargs):
    with ClusterRpcProxy(config) as cluster_rpc:
        return cluster_rpc.model_service.test(model_name, *args, **kwargs)


if __name__ == "__main__":
    from nlpwiz.service import client
    model = client.load_model(model_name="glove", dim=300)
    model.infer("cat")

    sims = model.invoke(model_name="glove", method_name="most_similar", params={"positive_words":["cat"]})

    similar_words = model.invoke(model_name="glove", method_name="most_similar", params={"positive_words": ["cat"]})


