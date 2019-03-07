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
  
  string authorizePayment (
    1: string cardNumber,
    2: double amount
  ),

  list<string> getTransactionHistory (
    1: string cardNumber
  ),

  string getCardNumbers ( ),

  bool postTransaction (
    1: string cardNumber,
    2: string description,
    3: double amount,
    4: string entryMode
  ),

  list<string> getTransactions (
    1: string cardNumber
    2: i16 numOfResults,
    3: string dateRange,
    4: string amountRange,
    5: string entryMode
  ),

  list<string> searchTransactions (
    1: string cardNumber,
    2: string description
  ),

  bool changeAuthorizationRule (
    1: string cardNumber,
    2: double amount
  )
}

// level-2 service
service TransactionHistory {
  
  list<string> getTransactionLog (
    1: string cardNumber
  ),

  list<string> filterTransactions (
    1: string cardNumber,
    2: i16 numOfResults,
    3: string dateRange,
    4: string amountRange,
    5: string entryMode,
    6: string description
  ),

  bool insertTransaction (
    1: string cardNumber,
    2: double amount,
    3: string entryMode,
    4: string description
  )

}

// Transaction History simulated DB 
service TransactionHistoryDB {
  
  list<string> getTransactionLog (
    1: string cardNumber
  ),
  
  bool insertTransaction (
    1: string cardNumber,
    2: double amount,
    3: string entryMode,
    4: string description
  )

}

// level-2 service
service PaymentAuthorization {

  bool authorize (
    1: string cardNumber,
    2: double amount
  ),

  bool changeAuthRule (
    1: string cardNumber,
    2: double newAmount
  )

}

// Authorization Rule simulated DB
service PaymentAuthorizationDB {
  
  double getLimit (
    1: string cardNumber
  ),

  bool changeLimit (
    1: string cardNumber,
    2: double newAmount
  )

  bool addLimit (
    1: string cardNumber,
    2: double amount
  )

}

// level-1 service
service CustomerInformation {
  
  map<string, string> retrieveContactInformation ( 
    1: string customerId
  ),

  bool updateContactInformation (
    1: string customerId,
    2: map<string,string> revisedInfo
  ),

  bool verifyContactInformation (
    1: string customerId,
    2: string field,
    3: string answer
  ),

  map<string, list<string>> getRegisteredProducts (
    1: string customerId
  ),

  list<string> getAccountNumbers (
    1: string customerId
  ),

  list<string> getCardNumbers (
    1: string customerId
  ),

  string newAccount (
    1: string customerId
  ),

  string newCard (
    1: string customerId
  ),
}

// level-2 service
service ContactInformation {

  map<string, string> retrieveCustomer (
    1: string customerId
  ),

  bool updateContactInformation (
    1: string customerId,
    2: map<string,string> revisedInfo
  )
}

// customer contact information simulated DB
service ContactInformationDB {
  
  map<string, string> retrieveCustomer (
    1: string customerId
  ),

  bool updateContactInformation (
    1: string customerId,
    2: map<string,string> revisedInfo
  )

}

// level-2 service
service RegisteredProducts {
  
  map<string, list<string>> getRegisteredProducts (
    1: string customerId
  )

  string addCard (
    1: string customerId
  ),

  string addAccount (
    1: string customerId
  )
}

// registered products simulated DB
service RegisteredProductsDB {
  
  list<string> getAccountNumbers (
    1: string customerId
  ),

  list<string> getCardNumbers (
    1: string customerId
  ),

  string addCard (
    1: string customerId
  ),

  string addAccount (
    1: string customerId
  )

}

// level-1 service
service OnlineBanking {
  string getAccountInformation(1: string customerId),
  string transferMoney(1: string fromAccountNumber, 2: string toAccountNumber, 3: i16 amount)
}

// level-2 service -- card management
// service PaymentAuthorization {
//   bool   authorize(1: string cardNumber, 2: i16 amount),
//   string getScheme(1: string cardNumber),
//   string changeScheme(1: string cardNumber)
// }

// level-2 service -- card management
// service TransactionHistory {
//   string getTransactionHistory(1: string cardNumber)
// }
