namespace cpp bank
namespace py bank

service HelloworldService {
  string getHelloworld()
}

service AuthenticateService {
  bool authenticate(1: string username, 2: string password)
}

service TransferService {
  string transfer()
}
