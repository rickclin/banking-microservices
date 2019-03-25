//
// Autogenerated by Thrift Compiler (0.10.0)
//
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
//
"use strict";

var thrift = require('thrift');
var Thrift = thrift.Thrift;
var Q = thrift.Q;


var ttypes = require('./bank_types');
//HELPER FUNCTIONS AND STRUCTURES

var TransactionHistory_getTransactionLog_args = function(args) {
  this.cardNumber = null;
  if (args) {
    if (args.cardNumber !== undefined && args.cardNumber !== null) {
      this.cardNumber = args.cardNumber;
    }
  }
};
TransactionHistory_getTransactionLog_args.prototype = {};
TransactionHistory_getTransactionLog_args.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.STRING) {
        this.cardNumber = input.readString();
      } else {
        input.skip(ftype);
      }
      break;
      case 0:
        input.skip(ftype);
        break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

TransactionHistory_getTransactionLog_args.prototype.write = function(output) {
  output.writeStructBegin('TransactionHistory_getTransactionLog_args');
  if (this.cardNumber !== null && this.cardNumber !== undefined) {
    output.writeFieldBegin('cardNumber', Thrift.Type.STRING, 1);
    output.writeString(this.cardNumber);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var TransactionHistory_getTransactionLog_result = function(args) {
  this.success = null;
  if (args) {
    if (args.success !== undefined && args.success !== null) {
      this.success = Thrift.copyList(args.success, [null]);
    }
  }
};
TransactionHistory_getTransactionLog_result.prototype = {};
TransactionHistory_getTransactionLog_result.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 0:
      if (ftype == Thrift.Type.LIST) {
        var _size24 = 0;
        var _rtmp328;
        this.success = [];
        var _etype27 = 0;
        _rtmp328 = input.readListBegin();
        _etype27 = _rtmp328.etype;
        _size24 = _rtmp328.size;
        for (var _i29 = 0; _i29 < _size24; ++_i29)
        {
          var elem30 = null;
          elem30 = input.readString();
          this.success.push(elem30);
        }
        input.readListEnd();
      } else {
        input.skip(ftype);
      }
      break;
      case 0:
        input.skip(ftype);
        break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

TransactionHistory_getTransactionLog_result.prototype.write = function(output) {
  output.writeStructBegin('TransactionHistory_getTransactionLog_result');
  if (this.success !== null && this.success !== undefined) {
    output.writeFieldBegin('success', Thrift.Type.LIST, 0);
    output.writeListBegin(Thrift.Type.STRING, this.success.length);
    for (var iter31 in this.success)
    {
      if (this.success.hasOwnProperty(iter31))
      {
        iter31 = this.success[iter31];
        output.writeString(iter31);
      }
    }
    output.writeListEnd();
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var TransactionHistory_filterTransactions_args = function(args) {
  this.cardNumber = null;
  this.numOfResults = null;
  this.dateRange = null;
  this.amountRange = null;
  this.entryMode = null;
  this.description = null;
  if (args) {
    if (args.cardNumber !== undefined && args.cardNumber !== null) {
      this.cardNumber = args.cardNumber;
    }
    if (args.numOfResults !== undefined && args.numOfResults !== null) {
      this.numOfResults = args.numOfResults;
    }
    if (args.dateRange !== undefined && args.dateRange !== null) {
      this.dateRange = args.dateRange;
    }
    if (args.amountRange !== undefined && args.amountRange !== null) {
      this.amountRange = args.amountRange;
    }
    if (args.entryMode !== undefined && args.entryMode !== null) {
      this.entryMode = args.entryMode;
    }
    if (args.description !== undefined && args.description !== null) {
      this.description = args.description;
    }
  }
};
TransactionHistory_filterTransactions_args.prototype = {};
TransactionHistory_filterTransactions_args.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.STRING) {
        this.cardNumber = input.readString();
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.I16) {
        this.numOfResults = input.readI16();
      } else {
        input.skip(ftype);
      }
      break;
      case 3:
      if (ftype == Thrift.Type.STRING) {
        this.dateRange = input.readString();
      } else {
        input.skip(ftype);
      }
      break;
      case 4:
      if (ftype == Thrift.Type.STRING) {
        this.amountRange = input.readString();
      } else {
        input.skip(ftype);
      }
      break;
      case 5:
      if (ftype == Thrift.Type.STRING) {
        this.entryMode = input.readString();
      } else {
        input.skip(ftype);
      }
      break;
      case 6:
      if (ftype == Thrift.Type.STRING) {
        this.description = input.readString();
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

TransactionHistory_filterTransactions_args.prototype.write = function(output) {
  output.writeStructBegin('TransactionHistory_filterTransactions_args');
  if (this.cardNumber !== null && this.cardNumber !== undefined) {
    output.writeFieldBegin('cardNumber', Thrift.Type.STRING, 1);
    output.writeString(this.cardNumber);
    output.writeFieldEnd();
  }
  if (this.numOfResults !== null && this.numOfResults !== undefined) {
    output.writeFieldBegin('numOfResults', Thrift.Type.I16, 2);
    output.writeI16(this.numOfResults);
    output.writeFieldEnd();
  }
  if (this.dateRange !== null && this.dateRange !== undefined) {
    output.writeFieldBegin('dateRange', Thrift.Type.STRING, 3);
    output.writeString(this.dateRange);
    output.writeFieldEnd();
  }
  if (this.amountRange !== null && this.amountRange !== undefined) {
    output.writeFieldBegin('amountRange', Thrift.Type.STRING, 4);
    output.writeString(this.amountRange);
    output.writeFieldEnd();
  }
  if (this.entryMode !== null && this.entryMode !== undefined) {
    output.writeFieldBegin('entryMode', Thrift.Type.STRING, 5);
    output.writeString(this.entryMode);
    output.writeFieldEnd();
  }
  if (this.description !== null && this.description !== undefined) {
    output.writeFieldBegin('description', Thrift.Type.STRING, 6);
    output.writeString(this.description);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var TransactionHistory_filterTransactions_result = function(args) {
  this.success = null;
  if (args) {
    if (args.success !== undefined && args.success !== null) {
      this.success = Thrift.copyList(args.success, [null]);
    }
  }
};
TransactionHistory_filterTransactions_result.prototype = {};
TransactionHistory_filterTransactions_result.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 0:
      if (ftype == Thrift.Type.LIST) {
        var _size32 = 0;
        var _rtmp336;
        this.success = [];
        var _etype35 = 0;
        _rtmp336 = input.readListBegin();
        _etype35 = _rtmp336.etype;
        _size32 = _rtmp336.size;
        for (var _i37 = 0; _i37 < _size32; ++_i37)
        {
          var elem38 = null;
          elem38 = input.readString();
          this.success.push(elem38);
        }
        input.readListEnd();
      } else {
        input.skip(ftype);
      }
      break;
      case 0:
        input.skip(ftype);
        break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

TransactionHistory_filterTransactions_result.prototype.write = function(output) {
  output.writeStructBegin('TransactionHistory_filterTransactions_result');
  if (this.success !== null && this.success !== undefined) {
    output.writeFieldBegin('success', Thrift.Type.LIST, 0);
    output.writeListBegin(Thrift.Type.STRING, this.success.length);
    for (var iter39 in this.success)
    {
      if (this.success.hasOwnProperty(iter39))
      {
        iter39 = this.success[iter39];
        output.writeString(iter39);
      }
    }
    output.writeListEnd();
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var TransactionHistory_insertTransaction_args = function(args) {
  this.cardNumber = null;
  this.amount = null;
  this.entryMode = null;
  this.description = null;
  if (args) {
    if (args.cardNumber !== undefined && args.cardNumber !== null) {
      this.cardNumber = args.cardNumber;
    }
    if (args.amount !== undefined && args.amount !== null) {
      this.amount = args.amount;
    }
    if (args.entryMode !== undefined && args.entryMode !== null) {
      this.entryMode = args.entryMode;
    }
    if (args.description !== undefined && args.description !== null) {
      this.description = args.description;
    }
  }
};
TransactionHistory_insertTransaction_args.prototype = {};
TransactionHistory_insertTransaction_args.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.STRING) {
        this.cardNumber = input.readString();
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.DOUBLE) {
        this.amount = input.readDouble();
      } else {
        input.skip(ftype);
      }
      break;
      case 3:
      if (ftype == Thrift.Type.STRING) {
        this.entryMode = input.readString();
      } else {
        input.skip(ftype);
      }
      break;
      case 4:
      if (ftype == Thrift.Type.STRING) {
        this.description = input.readString();
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

TransactionHistory_insertTransaction_args.prototype.write = function(output) {
  output.writeStructBegin('TransactionHistory_insertTransaction_args');
  if (this.cardNumber !== null && this.cardNumber !== undefined) {
    output.writeFieldBegin('cardNumber', Thrift.Type.STRING, 1);
    output.writeString(this.cardNumber);
    output.writeFieldEnd();
  }
  if (this.amount !== null && this.amount !== undefined) {
    output.writeFieldBegin('amount', Thrift.Type.DOUBLE, 2);
    output.writeDouble(this.amount);
    output.writeFieldEnd();
  }
  if (this.entryMode !== null && this.entryMode !== undefined) {
    output.writeFieldBegin('entryMode', Thrift.Type.STRING, 3);
    output.writeString(this.entryMode);
    output.writeFieldEnd();
  }
  if (this.description !== null && this.description !== undefined) {
    output.writeFieldBegin('description', Thrift.Type.STRING, 4);
    output.writeString(this.description);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var TransactionHistory_insertTransaction_result = function(args) {
  this.success = null;
  if (args) {
    if (args.success !== undefined && args.success !== null) {
      this.success = args.success;
    }
  }
};
TransactionHistory_insertTransaction_result.prototype = {};
TransactionHistory_insertTransaction_result.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 0:
      if (ftype == Thrift.Type.BOOL) {
        this.success = input.readBool();
      } else {
        input.skip(ftype);
      }
      break;
      case 0:
        input.skip(ftype);
        break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

TransactionHistory_insertTransaction_result.prototype.write = function(output) {
  output.writeStructBegin('TransactionHistory_insertTransaction_result');
  if (this.success !== null && this.success !== undefined) {
    output.writeFieldBegin('success', Thrift.Type.BOOL, 0);
    output.writeBool(this.success);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var TransactionHistoryClient = exports.Client = function(output, pClass) {
    this.output = output;
    this.pClass = pClass;
    this._seqid = 0;
    this._reqs = {};
};
TransactionHistoryClient.prototype = {};
TransactionHistoryClient.prototype.seqid = function() { return this._seqid; };
TransactionHistoryClient.prototype.new_seqid = function() { return this._seqid += 1; };
TransactionHistoryClient.prototype.getTransactionLog = function(cardNumber, callback) {
  this._seqid = this.new_seqid();
  if (callback === undefined) {
    var _defer = Q.defer();
    this._reqs[this.seqid()] = function(error, result) {
      if (error) {
        _defer.reject(error);
      } else {
        _defer.resolve(result);
      }
    };
    this.send_getTransactionLog(cardNumber);
    return _defer.promise;
  } else {
    this._reqs[this.seqid()] = callback;
    this.send_getTransactionLog(cardNumber);
  }
};

TransactionHistoryClient.prototype.send_getTransactionLog = function(cardNumber) {
  var output = new this.pClass(this.output);
  output.writeMessageBegin('getTransactionLog', Thrift.MessageType.CALL, this.seqid());
  var args = new TransactionHistory_getTransactionLog_args();
  args.cardNumber = cardNumber;
  args.write(output);
  output.writeMessageEnd();
  return this.output.flush();
};

TransactionHistoryClient.prototype.recv_getTransactionLog = function(input,mtype,rseqid) {
  var callback = this._reqs[rseqid] || function() {};
  delete this._reqs[rseqid];
  if (mtype == Thrift.MessageType.EXCEPTION) {
    var x = new Thrift.TApplicationException();
    x.read(input);
    input.readMessageEnd();
    return callback(x);
  }
  var result = new TransactionHistory_getTransactionLog_result();
  result.read(input);
  input.readMessageEnd();

  if (null !== result.success) {
    return callback(null, result.success);
  }
  return callback('getTransactionLog failed: unknown result');
};
TransactionHistoryClient.prototype.filterTransactions = function(cardNumber, numOfResults, dateRange, amountRange, entryMode, description, callback) {
  this._seqid = this.new_seqid();
  if (callback === undefined) {
    var _defer = Q.defer();
    this._reqs[this.seqid()] = function(error, result) {
      if (error) {
        _defer.reject(error);
      } else {
        _defer.resolve(result);
      }
    };
    this.send_filterTransactions(cardNumber, numOfResults, dateRange, amountRange, entryMode, description);
    return _defer.promise;
  } else {
    this._reqs[this.seqid()] = callback;
    this.send_filterTransactions(cardNumber, numOfResults, dateRange, amountRange, entryMode, description);
  }
};

TransactionHistoryClient.prototype.send_filterTransactions = function(cardNumber, numOfResults, dateRange, amountRange, entryMode, description) {
  var output = new this.pClass(this.output);
  output.writeMessageBegin('filterTransactions', Thrift.MessageType.CALL, this.seqid());
  var args = new TransactionHistory_filterTransactions_args();
  args.cardNumber = cardNumber;
  args.numOfResults = numOfResults;
  args.dateRange = dateRange;
  args.amountRange = amountRange;
  args.entryMode = entryMode;
  args.description = description;
  args.write(output);
  output.writeMessageEnd();
  return this.output.flush();
};

TransactionHistoryClient.prototype.recv_filterTransactions = function(input,mtype,rseqid) {
  var callback = this._reqs[rseqid] || function() {};
  delete this._reqs[rseqid];
  if (mtype == Thrift.MessageType.EXCEPTION) {
    var x = new Thrift.TApplicationException();
    x.read(input);
    input.readMessageEnd();
    return callback(x);
  }
  var result = new TransactionHistory_filterTransactions_result();
  result.read(input);
  input.readMessageEnd();

  if (null !== result.success) {
    return callback(null, result.success);
  }
  return callback('filterTransactions failed: unknown result');
};
TransactionHistoryClient.prototype.insertTransaction = function(cardNumber, amount, entryMode, description, callback) {
  this._seqid = this.new_seqid();
  if (callback === undefined) {
    var _defer = Q.defer();
    this._reqs[this.seqid()] = function(error, result) {
      if (error) {
        _defer.reject(error);
      } else {
        _defer.resolve(result);
      }
    };
    this.send_insertTransaction(cardNumber, amount, entryMode, description);
    return _defer.promise;
  } else {
    this._reqs[this.seqid()] = callback;
    this.send_insertTransaction(cardNumber, amount, entryMode, description);
  }
};

TransactionHistoryClient.prototype.send_insertTransaction = function(cardNumber, amount, entryMode, description) {
  var output = new this.pClass(this.output);
  output.writeMessageBegin('insertTransaction', Thrift.MessageType.CALL, this.seqid());
  var args = new TransactionHistory_insertTransaction_args();
  args.cardNumber = cardNumber;
  args.amount = amount;
  args.entryMode = entryMode;
  args.description = description;
  args.write(output);
  output.writeMessageEnd();
  return this.output.flush();
};

TransactionHistoryClient.prototype.recv_insertTransaction = function(input,mtype,rseqid) {
  var callback = this._reqs[rseqid] || function() {};
  delete this._reqs[rseqid];
  if (mtype == Thrift.MessageType.EXCEPTION) {
    var x = new Thrift.TApplicationException();
    x.read(input);
    input.readMessageEnd();
    return callback(x);
  }
  var result = new TransactionHistory_insertTransaction_result();
  result.read(input);
  input.readMessageEnd();

  if (null !== result.success) {
    return callback(null, result.success);
  }
  return callback('insertTransaction failed: unknown result');
};
var TransactionHistoryProcessor = exports.Processor = function(handler) {
  this._handler = handler;
}
;
TransactionHistoryProcessor.prototype.process = function(input, output) {
  var r = input.readMessageBegin();
  if (this['process_' + r.fname]) {
    return this['process_' + r.fname].call(this, r.rseqid, input, output);
  } else {
    input.skip(Thrift.Type.STRUCT);
    input.readMessageEnd();
    var x = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN_METHOD, 'Unknown function ' + r.fname);
    output.writeMessageBegin(r.fname, Thrift.MessageType.EXCEPTION, r.rseqid);
    x.write(output);
    output.writeMessageEnd();
    output.flush();
  }
}
;
TransactionHistoryProcessor.prototype.process_getTransactionLog = function(seqid, input, output) {
  var args = new TransactionHistory_getTransactionLog_args();
  args.read(input);
  input.readMessageEnd();
  if (this._handler.getTransactionLog.length === 1) {
    Q.fcall(this._handler.getTransactionLog, args.cardNumber)
      .then(function(result) {
        var result_obj = new TransactionHistory_getTransactionLog_result({success: result});
        output.writeMessageBegin("getTransactionLog", Thrift.MessageType.REPLY, seqid);
        result_obj.write(output);
        output.writeMessageEnd();
        output.flush();
      }, function (err) {
        var result;
        result = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
        output.writeMessageBegin("getTransactionLog", Thrift.MessageType.EXCEPTION, seqid);
        result.write(output);
        output.writeMessageEnd();
        output.flush();
      });
  } else {
    this._handler.getTransactionLog(args.cardNumber, function (err, result) {
      var result_obj;
      if ((err === null || typeof err === 'undefined')) {
        result_obj = new TransactionHistory_getTransactionLog_result((err !== null || typeof err === 'undefined') ? err : {success: result});
        output.writeMessageBegin("getTransactionLog", Thrift.MessageType.REPLY, seqid);
      } else {
        result_obj = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
        output.writeMessageBegin("getTransactionLog", Thrift.MessageType.EXCEPTION, seqid);
      }
      result_obj.write(output);
      output.writeMessageEnd();
      output.flush();
    });
  }
};
TransactionHistoryProcessor.prototype.process_filterTransactions = function(seqid, input, output) {
  var args = new TransactionHistory_filterTransactions_args();
  args.read(input);
  input.readMessageEnd();
  if (this._handler.filterTransactions.length === 6) {
    Q.fcall(this._handler.filterTransactions, args.cardNumber, args.numOfResults, args.dateRange, args.amountRange, args.entryMode, args.description)
      .then(function(result) {
        var result_obj = new TransactionHistory_filterTransactions_result({success: result});
        output.writeMessageBegin("filterTransactions", Thrift.MessageType.REPLY, seqid);
        result_obj.write(output);
        output.writeMessageEnd();
        output.flush();
      }, function (err) {
        var result;
        result = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
        output.writeMessageBegin("filterTransactions", Thrift.MessageType.EXCEPTION, seqid);
        result.write(output);
        output.writeMessageEnd();
        output.flush();
      });
  } else {
    this._handler.filterTransactions(args.cardNumber, args.numOfResults, args.dateRange, args.amountRange, args.entryMode, args.description, function (err, result) {
      var result_obj;
      if ((err === null || typeof err === 'undefined')) {
        result_obj = new TransactionHistory_filterTransactions_result((err !== null || typeof err === 'undefined') ? err : {success: result});
        output.writeMessageBegin("filterTransactions", Thrift.MessageType.REPLY, seqid);
      } else {
        result_obj = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
        output.writeMessageBegin("filterTransactions", Thrift.MessageType.EXCEPTION, seqid);
      }
      result_obj.write(output);
      output.writeMessageEnd();
      output.flush();
    });
  }
};
TransactionHistoryProcessor.prototype.process_insertTransaction = function(seqid, input, output) {
  var args = new TransactionHistory_insertTransaction_args();
  args.read(input);
  input.readMessageEnd();
  if (this._handler.insertTransaction.length === 4) {
    Q.fcall(this._handler.insertTransaction, args.cardNumber, args.amount, args.entryMode, args.description)
      .then(function(result) {
        var result_obj = new TransactionHistory_insertTransaction_result({success: result});
        output.writeMessageBegin("insertTransaction", Thrift.MessageType.REPLY, seqid);
        result_obj.write(output);
        output.writeMessageEnd();
        output.flush();
      }, function (err) {
        var result;
        result = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
        output.writeMessageBegin("insertTransaction", Thrift.MessageType.EXCEPTION, seqid);
        result.write(output);
        output.writeMessageEnd();
        output.flush();
      });
  } else {
    this._handler.insertTransaction(args.cardNumber, args.amount, args.entryMode, args.description, function (err, result) {
      var result_obj;
      if ((err === null || typeof err === 'undefined')) {
        result_obj = new TransactionHistory_insertTransaction_result((err !== null || typeof err === 'undefined') ? err : {success: result});
        output.writeMessageBegin("insertTransaction", Thrift.MessageType.REPLY, seqid);
      } else {
        result_obj = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
        output.writeMessageBegin("insertTransaction", Thrift.MessageType.EXCEPTION, seqid);
      }
      result_obj.write(output);
      output.writeMessageEnd();
      output.flush();
    });
  }
};