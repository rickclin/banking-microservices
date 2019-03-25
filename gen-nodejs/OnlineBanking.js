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

var OnlineBanking_getBalance_args = function(args) {
  this.accountNumber = null;
  if (args) {
    if (args.accountNumber !== undefined && args.accountNumber !== null) {
      this.accountNumber = args.accountNumber;
    }
  }
};
OnlineBanking_getBalance_args.prototype = {};
OnlineBanking_getBalance_args.prototype.read = function(input) {
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
        this.accountNumber = input.readString();
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

OnlineBanking_getBalance_args.prototype.write = function(output) {
  output.writeStructBegin('OnlineBanking_getBalance_args');
  if (this.accountNumber !== null && this.accountNumber !== undefined) {
    output.writeFieldBegin('accountNumber', Thrift.Type.STRING, 1);
    output.writeString(this.accountNumber);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var OnlineBanking_getBalance_result = function(args) {
  this.success = null;
  if (args) {
    if (args.success !== undefined && args.success !== null) {
      this.success = args.success;
    }
  }
};
OnlineBanking_getBalance_result.prototype = {};
OnlineBanking_getBalance_result.prototype.read = function(input) {
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
      if (ftype == Thrift.Type.STRING) {
        this.success = input.readString();
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

OnlineBanking_getBalance_result.prototype.write = function(output) {
  output.writeStructBegin('OnlineBanking_getBalance_result');
  if (this.success !== null && this.success !== undefined) {
    output.writeFieldBegin('success', Thrift.Type.STRING, 0);
    output.writeString(this.success);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var OnlineBanking_transferMoney_args = function(args) {
  this.fromAccount = null;
  this.toAccount = null;
  this.amount = null;
  if (args) {
    if (args.fromAccount !== undefined && args.fromAccount !== null) {
      this.fromAccount = args.fromAccount;
    }
    if (args.toAccount !== undefined && args.toAccount !== null) {
      this.toAccount = args.toAccount;
    }
    if (args.amount !== undefined && args.amount !== null) {
      this.amount = args.amount;
    }
  }
};
OnlineBanking_transferMoney_args.prototype = {};
OnlineBanking_transferMoney_args.prototype.read = function(input) {
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
        this.fromAccount = input.readString();
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.STRING) {
        this.toAccount = input.readString();
      } else {
        input.skip(ftype);
      }
      break;
      case 3:
      if (ftype == Thrift.Type.STRING) {
        this.amount = input.readString();
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

OnlineBanking_transferMoney_args.prototype.write = function(output) {
  output.writeStructBegin('OnlineBanking_transferMoney_args');
  if (this.fromAccount !== null && this.fromAccount !== undefined) {
    output.writeFieldBegin('fromAccount', Thrift.Type.STRING, 1);
    output.writeString(this.fromAccount);
    output.writeFieldEnd();
  }
  if (this.toAccount !== null && this.toAccount !== undefined) {
    output.writeFieldBegin('toAccount', Thrift.Type.STRING, 2);
    output.writeString(this.toAccount);
    output.writeFieldEnd();
  }
  if (this.amount !== null && this.amount !== undefined) {
    output.writeFieldBegin('amount', Thrift.Type.STRING, 3);
    output.writeString(this.amount);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var OnlineBanking_transferMoney_result = function(args) {
  this.success = null;
  if (args) {
    if (args.success !== undefined && args.success !== null) {
      this.success = args.success;
    }
  }
};
OnlineBanking_transferMoney_result.prototype = {};
OnlineBanking_transferMoney_result.prototype.read = function(input) {
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

OnlineBanking_transferMoney_result.prototype.write = function(output) {
  output.writeStructBegin('OnlineBanking_transferMoney_result');
  if (this.success !== null && this.success !== undefined) {
    output.writeFieldBegin('success', Thrift.Type.BOOL, 0);
    output.writeBool(this.success);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var OnlineBankingClient = exports.Client = function(output, pClass) {
    this.output = output;
    this.pClass = pClass;
    this._seqid = 0;
    this._reqs = {};
};
OnlineBankingClient.prototype = {};
OnlineBankingClient.prototype.seqid = function() { return this._seqid; };
OnlineBankingClient.prototype.new_seqid = function() { return this._seqid += 1; };
OnlineBankingClient.prototype.getBalance = function(accountNumber, callback) {
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
    this.send_getBalance(accountNumber);
    return _defer.promise;
  } else {
    this._reqs[this.seqid()] = callback;
    this.send_getBalance(accountNumber);
  }
};

OnlineBankingClient.prototype.send_getBalance = function(accountNumber) {
  var output = new this.pClass(this.output);
  output.writeMessageBegin('getBalance', Thrift.MessageType.CALL, this.seqid());
  var args = new OnlineBanking_getBalance_args();
  args.accountNumber = accountNumber;
  args.write(output);
  output.writeMessageEnd();
  return this.output.flush();
};

OnlineBankingClient.prototype.recv_getBalance = function(input,mtype,rseqid) {
  var callback = this._reqs[rseqid] || function() {};
  delete this._reqs[rseqid];
  if (mtype == Thrift.MessageType.EXCEPTION) {
    var x = new Thrift.TApplicationException();
    x.read(input);
    input.readMessageEnd();
    return callback(x);
  }
  var result = new OnlineBanking_getBalance_result();
  result.read(input);
  input.readMessageEnd();

  if (null !== result.success) {
    return callback(null, result.success);
  }
  return callback('getBalance failed: unknown result');
};
OnlineBankingClient.prototype.transferMoney = function(fromAccount, toAccount, amount, callback) {
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
    this.send_transferMoney(fromAccount, toAccount, amount);
    return _defer.promise;
  } else {
    this._reqs[this.seqid()] = callback;
    this.send_transferMoney(fromAccount, toAccount, amount);
  }
};

OnlineBankingClient.prototype.send_transferMoney = function(fromAccount, toAccount, amount) {
  var output = new this.pClass(this.output);
  output.writeMessageBegin('transferMoney', Thrift.MessageType.CALL, this.seqid());
  var args = new OnlineBanking_transferMoney_args();
  args.fromAccount = fromAccount;
  args.toAccount = toAccount;
  args.amount = amount;
  args.write(output);
  output.writeMessageEnd();
  return this.output.flush();
};

OnlineBankingClient.prototype.recv_transferMoney = function(input,mtype,rseqid) {
  var callback = this._reqs[rseqid] || function() {};
  delete this._reqs[rseqid];
  if (mtype == Thrift.MessageType.EXCEPTION) {
    var x = new Thrift.TApplicationException();
    x.read(input);
    input.readMessageEnd();
    return callback(x);
  }
  var result = new OnlineBanking_transferMoney_result();
  result.read(input);
  input.readMessageEnd();

  if (null !== result.success) {
    return callback(null, result.success);
  }
  return callback('transferMoney failed: unknown result');
};
var OnlineBankingProcessor = exports.Processor = function(handler) {
  this._handler = handler;
}
;
OnlineBankingProcessor.prototype.process = function(input, output) {
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
OnlineBankingProcessor.prototype.process_getBalance = function(seqid, input, output) {
  var args = new OnlineBanking_getBalance_args();
  args.read(input);
  input.readMessageEnd();
  if (this._handler.getBalance.length === 1) {
    Q.fcall(this._handler.getBalance, args.accountNumber)
      .then(function(result) {
        var result_obj = new OnlineBanking_getBalance_result({success: result});
        output.writeMessageBegin("getBalance", Thrift.MessageType.REPLY, seqid);
        result_obj.write(output);
        output.writeMessageEnd();
        output.flush();
      }, function (err) {
        var result;
        result = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
        output.writeMessageBegin("getBalance", Thrift.MessageType.EXCEPTION, seqid);
        result.write(output);
        output.writeMessageEnd();
        output.flush();
      });
  } else {
    this._handler.getBalance(args.accountNumber, function (err, result) {
      var result_obj;
      if ((err === null || typeof err === 'undefined')) {
        result_obj = new OnlineBanking_getBalance_result((err !== null || typeof err === 'undefined') ? err : {success: result});
        output.writeMessageBegin("getBalance", Thrift.MessageType.REPLY, seqid);
      } else {
        result_obj = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
        output.writeMessageBegin("getBalance", Thrift.MessageType.EXCEPTION, seqid);
      }
      result_obj.write(output);
      output.writeMessageEnd();
      output.flush();
    });
  }
};
OnlineBankingProcessor.prototype.process_transferMoney = function(seqid, input, output) {
  var args = new OnlineBanking_transferMoney_args();
  args.read(input);
  input.readMessageEnd();
  if (this._handler.transferMoney.length === 3) {
    Q.fcall(this._handler.transferMoney, args.fromAccount, args.toAccount, args.amount)
      .then(function(result) {
        var result_obj = new OnlineBanking_transferMoney_result({success: result});
        output.writeMessageBegin("transferMoney", Thrift.MessageType.REPLY, seqid);
        result_obj.write(output);
        output.writeMessageEnd();
        output.flush();
      }, function (err) {
        var result;
        result = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
        output.writeMessageBegin("transferMoney", Thrift.MessageType.EXCEPTION, seqid);
        result.write(output);
        output.writeMessageEnd();
        output.flush();
      });
  } else {
    this._handler.transferMoney(args.fromAccount, args.toAccount, args.amount, function (err, result) {
      var result_obj;
      if ((err === null || typeof err === 'undefined')) {
        result_obj = new OnlineBanking_transferMoney_result((err !== null || typeof err === 'undefined') ? err : {success: result});
        output.writeMessageBegin("transferMoney", Thrift.MessageType.REPLY, seqid);
      } else {
        result_obj = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
        output.writeMessageBegin("transferMoney", Thrift.MessageType.EXCEPTION, seqid);
      }
      result_obj.write(output);
      output.writeMessageEnd();
      output.flush();
    });
  }
};