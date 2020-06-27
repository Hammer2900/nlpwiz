
from nameko.rpc import rpc

from nlpwiz import model_factory

class ModelsService:
    name = "model_service"

    @rpc
    def invoke(self, model_name, method_name, params, model_params={}):
        method = getattr(model_factory, "invoke")
        return method(model_name, method_name=method_name, params=params, model_params=model_params)

    @rpc
    def infer(self, model_name, params, model_params={}):
        return self.invoke(model_name, method_name="infer", params=params, model_params=model_params)

    @rpc
    def test(self, model_name, *args, **kwargs):
        #with ClusterRpcProxy(config) as cluster_rpc:
        #    return cluster_rpc.model_service.infer(model_name, *args, **kwargs)
        return "test method"


if __name__ == "__main__":
    pass