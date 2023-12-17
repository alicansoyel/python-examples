from custom_protocol.abstract.ProtocolRepository import ProtocolRepository

class ProtocolCategoryRepository(ProtocolRepository):

    def save(self)->None:
        print("Category added...")

    def delete(self)->None:
        print("Category deleted...")

    def update(self)->None:
        print("Category updated...")

    def get_all(self)->None:
        print("Category list...")

    def get_by_id(self)->None:
        print("Category by id...")