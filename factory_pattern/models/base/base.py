import abc

class BaseRunnable:

    @abc.abstractmethod
    def run(self)->None:
        """
        Run the execution flow
        :return:_
        """
        raise NotImplementedError

    def set_params(self, params)->None:
        for k, v in params.items():
            setattr(self, k, v)