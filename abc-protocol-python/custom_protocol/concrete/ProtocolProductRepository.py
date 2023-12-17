from custom_protocol.abstract.ProtocolRepository import ProtocolRepository

class ProtocolProductRepository(ProtocolRepository):

    """def save(self)->None:
        print("Product added...")"""

    def delete(self)->None:
        print("Product deleted...")

    def update(self)->None:
        print("Product updated...")

    def get_all(self)->None:
        print("Product list...")

    def get_by_id(self)->None:
        print("Product by id...")

