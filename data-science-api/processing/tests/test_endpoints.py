import pytest
import api.v0_1

from tests import PySparkUnittestBase


class TestEndpoint(PySparkUnittestBase):

    # TODO: This is just a template. Remove this class once you start working on the unit tests

    @classmethod
    def setup_class(cls):
        super().setup_class()

    @pytest.mark.skip(reason="functionality has not yet been implemented")
    def test_get_n_most_similar_docs(self):
        """ Make sure the endpoint returns
        """

        n = 4
        json_input = {"tipo_documento": "lei", "link_documento": "...."}

        response = self.client.post("/get_docs_similares?n=%d" % n, json=json_input)

        assert response.status_code == 200, (
            "Endpoint should have returned a HTTP status code 200."
            + "\nResponse JSON = %s" % response.json()
        )

        # TODO: Implement other asserts
        raise NotImplementedError()

    @pytest.mark.skip(reason="functionality has not yet been implemented")
    def test_get_most_similar_docs_default_threshold(self):
        """ Make sure the endpoint returns
        """
        json_input = {"tipo_documento": "lei", "link_documento": "...."}

        response = self.client.post("/get_docs_similares", json=json_input)

        assert response.status_code == 200, (
            "Endpoint should have returned a HTTP status code 200."
            + "\nResponse JSON = %s" % response.json()
        )

        # TODO: Implement other asserts
        raise NotImplementedError()

    @pytest.mark.skip(reason="functionality has not yet been implemented")
    def test_get_most_similar_docs_user_informed_threshold(self):
        """ Make sure the endpoint returns
        """

        threshold = 0.1
        json_input = {"tipo_documento": "lei", "link_documento": "...."}

        response = self.client.post("/get_docs_similares?threshold=%f" % threshold, json=json_input)

        assert response.status_code == 200, (
            "Endpoint should have returned a HTTP status code 200."
            + "\nResponse JSON = %s" % response.json()
        )

        # TODO: Implement other asserts
        raise NotImplementedError()
