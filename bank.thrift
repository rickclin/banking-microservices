namespace cpp   bank
namespace py    bank
namespace java  bank

service HelloworldService {
  string getHelloworld()
}

service AuthenticateService {
  bool authenticate(1: string username, 2: string password)
}

// level-1 service
service CardManagement {
  string authorizePayment(1: string cardNumber, 2: double amount),
  list<string> getTransactionHistory(1: string cardNumber),
  string getCardNumber()
}

// level-1 service
service CustomerInformation {
  map<string, string> getContactInformation(1: string customerId),
  list<string> getRegisteredProducts(1: string customerId)
}

// level-1 service
service OnlineBanking {
  string getAccountInformation(1: string customerId),
  string transferMoney(1: string fromAccountNumber, 2: string toAccountNumber, 3: i16 amount)
}

// level-2 service -- card management
service PaymentAuthorization {
  bool   authorize(1: string cardNumber, 2: i16 amount),
  string getScheme(1: string cardNumber),
  string changeScheme(1: string cardNumber)
}

// level-2 service -- card management
service TransactionHistory {
  string getTransactionHistory(1: string cardNumber)
}
