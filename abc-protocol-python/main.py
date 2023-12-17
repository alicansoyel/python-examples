from custom_abc.concrete.ABCProductRepository import ABCProductRepository
from custom_abc.concrete.ABCCategoryRepository import ABCCategoryRepository
from custom_protocol.concrete.ProtocolProductRepository import ProtocolProductRepository
from custom_protocol.concrete.ProtocolCategoryRepository import ProtocolCategoryRepository


def main()->None:

    #ABC examples
    abc_product_repository = ABCProductRepository()
    abc_product_repository.save()
    abc_product_repository.delete()
    abc_product_repository.update()
    abc_product_repository.get_all()
    abc_product_repository.get_by_id()

    abc_category_repository = ABCCategoryRepository()
    abc_category_repository.save()
    abc_category_repository.delete()
    abc_category_repository.update()
    abc_category_repository.get_all()
    abc_category_repository.get_by_id()
    


    #Protocol examples
    protocol_product_repository = ProtocolProductRepository()
    protocol_product_repository.save()
    protocol_product_repository.delete()
    protocol_product_repository.update()
    protocol_product_repository.get_all()
    protocol_product_repository.get_by_id()

    protocol_category_repository = ProtocolCategoryRepository()
    protocol_category_repository.save()
    protocol_category_repository.delete()
    protocol_category_repository.update()
    protocol_category_repository.get_all()
    protocol_category_repository.get_by_id()



if __name__ == "__main__":
    main()