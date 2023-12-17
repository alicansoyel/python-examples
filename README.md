# Python Örnekleri

Bu repository, Python'da kullanılan bazı kod örneklerini içermektedir.

1. ***ABC(Abstract Base Class) ve Protocol***
   
   ABC (Abstract Base Class) ve Protocol, Python programlamasında soyutlamayı sağlamak için yaygın olarak kullanılan yapılar arasındadır. Bir ABC tanımlandığında, ilgili sınıf ABC'den referans alır ve ilgili metotlar @abstractmethod dekoratörü ile işaretlenir. Daha sonra, bu sınıftan türeyen diğer sınıflar, ABC içinde bulunan metotları uygulamak zorundadır. Bu, kesin bir bağlılık anlamına gelir ve bir tür sözleşme oluşturur. Kısacası, ilgili sınıf, ABC'ye ait metotları kullanmayı taahhüt eder.
   
   Protocol yapısında ise ilgili soyut sınıf, Protocol'den referans alır ve metotların içeriğini ABC'de olduğu gibi boş bırakır. Diğer sınıflar, Protocol'den referans alsın veya almasın, tüm metotları uygulamak zorunda değildir. Bu, daha esnek bir yapı oluşturarak sınıflar arasında daha az katı bir bağlantı sağlar.

****************************************************************************************************************************************************************************************************************************************************************************
# Python Examples

This repository contains some code examples used in Python.

1. ***ABC(Abstract Base Class) and Protocol***

   ABC (Abstract Base Class) and Protocol are commonly used structures in Python programming to facilitate abstraction. When an ABC is defined, the relevant class inherits from ABC, and the relevant methods are marked with the @abstractmethod decorator. Subsequently, other classes derived from this class are required to implement the methods defined in the ABC. This implies a strict commitment and establishes a sort of contract. In short, the relevant class commits to using the methods defined in the ABC.

   In the Protocol structure, the corresponding abstract class inherits from Protocol and leaves the content of methods empty, similar to the ABC. Other classes, whether they inherit from Protocol or not, are not obliged to implement all methods. This allows for a more flexible structure, providing less rigid connection between classes.

