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

var AccountInformationDB_getBalance_args = function(args) {
  this.accountNumber = null;
  if (args) {
    if (args.accountNumber !== undefined && args.accountNumber !== null) {
      this.accountNumber = args.accountNumber;
    }
  }
};
AccountInformationDB_getBalance_args.prototype = {};
AccountInformationDB_getBalance_args.prototype.read = function(input) {
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

AccountInformationDB_getBalance_args.prototype.write = function(output) {
  output.writeStructBegin('AccountInformationDB_getBalance_args');
  if (this.accountNumber !== null && this.accountNumber !== undefined) {
    output.writeFieldBegin('accountNumber', Thrift.Type.STRING, 1);
    output.writeString(this.accountNumber);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var AccountInformationDB_getBalance_result = function(args) {
  this.success = null;
  if (args) {
    if (args.success !== undefined && args.success !== null) {
      this.success = args.success;
    }
  }
};
AccountInformationDB_getBalance_result.prototype = {};
AccountInformationDB_getBalance_result.prototype.read = function(input) {
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

AccountInformationDB_getBalance_result.prototype.write = function(output) {
  output.writeStructBegin('AccountInformationDB_getBalance_result');
  if (this.success !== null && this.success !== undefined) {
    output.writeFieldBegin('success', Thrift.Type.STRING, 0);
    output.writeString(this.success);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var AccountInformationDB_updateBalance_args = function(args) {
  this.accountNumber = null;
  this.amount = null;
  if (args) {
    if (args.accountNumber !== undefined && args.accountNumber !== null) {
      this.accountNumber = args.accountNumber;
    }
    if (args.amount !== undefined && args.amount !== null) {
      this.amount = args.amount;
    }
  }
};
AccountInformationDB_updateBalance_args.prototype = {};
AccountInformationDB_updateBalance_args.prototype.read = function(input) {
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
      case 2:
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

AccountInformationDB_updateBalance_args.prototype.write = function(output) {
  output.writeStructBegin('AccountInformationDB_updateBalance_args');
  if (this.accountNumber !== null && this.accountNumber !== undefined) {
    output.writeFieldBegin('accountNumber', Thrift.Type.STRING, 1);
    output.writeString(this.accountNumber);
    output.writeFieldEnd();
  }
  if (this.amount !== null && this.amount !== undefined) {
    output.writeFieldBegin('amount', Thrift.Type.STRING, 2);
    output.writeString(this.amount);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var AccountInformationDB_updateBalance_result = function(args) {
  this.success = null;
  if (args) {
    if (args.success !== undefined && args.success !== null) {
      this.success = args.success;
    }
  }
};
AccountInformationDB_updateBalance_result.prototype = {};
AccountInformationDB_updateBalance_result.prototype.read = function(input) {
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

AccountInformationDB_updateBalance_result.prototype.write = function(output) {
  output.writeStructBegin('AccountInformationDB_updateBalance_result');
  if (this.success !== null && this.success !== undefined) {
    output.writeFieldBegin('success', Thrift.Type.STRING, 0);
    output.writeString(this.success);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var AccountInformationDB_addAccount_args = function(args) {
  this.accountNumber = null;
  if (args) {
    if (args.accountNumber !== undefined && args.accountNumber !== null) {
      this.accountNumber = args.accountNumber;
    }
  }
};
AccountInformationDB_addAccount_args.prototype = {};
AccountInformationDB_addAccount_args.prototype.read = function(input) {
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

AccountInformationDB_addAccount_args.prototype.write = function(output) {
  output.writeStructBegin('AccountInformationDB_addAccount_args');
  if (this.accountNumber !== null && this.accountNumber !== undefined) {
    output.writeFieldBegin('accountNumber', Thrift.Type.STRING, 1);
    output.writeString(this.accountNumber);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var AccountInformationDB_addAccount_result = function(args) {
  this.success = null;
  if (args) {
    if (args.success !== undefined && args.success !== null) {
      this.success = args.success;
    }
  }
};
AccountInformationDB_addAccount_result.prototype = {};
AccountInformationDB_addAccount_result.prototype.read = function(input) {
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

AccountInformationDB_addAccount_result.prototype.write = function(output) {
  output.writeStructBegin('AccountInformationDB_addAccount_result');
  if (this.success !== null && this.success !== undefined) {
    output.writeFieldBegin('success', Thrift.Type.BOOL, 0);
    output.writeBool(this.success);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var AccountInformationDBClient = exports.Client = function(output, pClass) {
    this.output = output;
    this.pClass = pClass;
    this._seqid = 0;
    this._reqs = {};
};
AccountInformationDBClient.prototype = {};
AccountInformationDBClient.prototype.seqid = function() { return this._seqid; };
AccountInformationDBClient.prototype.new_seqid = function() { return this._seqid += 1; };
AccountInformationDBClient.prototype.getBalance = function(accountNumber, callback) {
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

AccountInformationDBClient.prototype.send_getBalance = function(accountNumber) {
  var output = new this.pClass(this.output);
  output.writeMessageBegin('getBalance', Thrift.MessageType.CALL, this.seqid());
  var args = new AccountInformationDB_getBalance_args();
  args.accountNumber = accountNumber;
  args.write(output);
  output.writeMessageEnd();
  return this.output.flush();
};

AccountInformationDBClient.prototype.recv_getBalance = function(input,mtype,rseqid) {
  var callback = this._reqs[rseqid] || function() {};
  delete this._reqs[rseqid];
  if (mtype == Thrift.MessageType.EXCEPTION) {
    var x = new Thrift.TApplicationException();
    x.read(input);
    input.readMessageEnd();
    return callback(x);
  }
  var result = new AccountInformationDB_getBalance_result();
  result.read(input);
  input.readMessageEnd();

  if (null !== result.success) {
    return callback(null, result.success);
  }
  return callback('getBalance failed: unknown result');
};
AccountInformationDBClient.prototype.updateBalance = function(accountNumber, amount, callback) {
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
    this.send_updateBalance(accountNumber, amount);
    return _defer.promise;
  } else {
    this._reqs[this.seqid()] = callback;
    this.send_updateBalance(accountNumber, amount);
  }
};

AccountInformationDBClient.prototype.send_updateBalance = function(accountNumber, amount) {
  var output = new this.pClass(this.output);
  output.writeMessageBegin('updateBalance', Thrift.MessageType.CALL, this.seqid());
  var args = new AccountInformationDB_updateBalance_args();
  args.accountNumber = accountNumber;
  args.amount = amount;
  args.write(output);
  output.writeMessageEnd();
  return this.output.flush();
};

AccountInformationDBClient.prototype.recv_updateBalance = function(input,mtype,rseqid) {
  var callback = this._reqs[rseqid] || function() {};
  delete this._reqs[rseqid];
  if (mtype == Thrift.MessageType.EXCEPTION) {
    var x = new Thrift.TApplicationException();
    x.read(input);
    input.readMessageEnd();
    return callback(x);
  }
  var result = new AccountInformationDB_updateBalance_result();
  result.read(input);
  input.readMessageEnd();

  if (null !== result.success) {
    return callback(null, result.success);
  }
  return callback('updateBalance failed: unknown result');
};
AccountInformationDBClient.prototype.addAccount = function(accountNumber, callback) {
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
    this.send_addAccount(accountNumber);
    return _defer.promise;
  } else {
    this._reqs[this.seqid()] = callback;
    this.send_addAccount(accountNumber);
  }
};

AccountInformationDBClient.prototype.send_addAccount = function(accountNumber) {
  var output = new this.pClass(this.output);
  output.writeMessageBegin('addAccount', Thrift.MessageType.CALL, this.seqid());
  var args = new AccountInformationDB_addAccount_args();
  args.accountNumber = accountNumber;
  args.write(output);
  output.writeMessageEnd();
  return this.output.flush();
};

AccountInformationDBClient.prototype.recv_addAccount = function(input,mtype,rseqid) {
  var callback = this._reqs[rseqid] || function() {};
  delete this._reqs[rseqid];
  if (mtype == Thrift.MessageType.EXCEPTION) {
    var x = new Thrift.TApplicationException();
    x.read(input);
    input.readMessageEnd();
    return callback(x);
  }
  var result = new AccountInformationDB_addAccount_result();
  result.read(input);
  input.readMessageEnd();

  if (null !== result.success) {
    return callback(null, result.success);
  }
  return callback('addAccount failed: unknown result');
};
var AccountInformationDBProcessor = exports.Processor = function(handler) {
  this._handler = handler;
}
;
AccountInformationDBProcessor.prototype.process = function(input, output) {
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
AccountInformationDBProcessor.prototype.process_getBalance = function(seqid, input, output) {
  var args = new AccountInformationDB_getBalance_args();
  args.read(input);
  input.readMessageEnd();
  if (this._handler.getBalance.length === 1) {
    Q.fcall(this._handler.getBalance, args.accountNumber)
      .then(function(result) {
        var result_obj = new AccountInformationDB_getBalance_result({success: result});
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
        result_obj = new AccountInformationDB_getBalance_result((err !== null || typeof err === 'undefined') ? err : {success: result});
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
AccountInformationDBProcessor.prototype.process_updateBalance = function(seqid, input, output) {
  var args = new AccountInformationDB_updateBalance_args();
  args.read(input);
  input.readMessageEnd();
  if (this._handler.updateBalance.length === 2) {
    Q.fcall(this._handler.updateBalance, args.accountNumber, args.amount)
      .then(function(result) {
        var result_obj = new AccountInformationDB_updateBalance_result({success: result});
        output.writeMessageBegin("updateBalance", Thrift.MessageType.REPLY, seqid);
        result_obj.write(output);
        output.writeMessageEnd();
        output.flush();
      }, function (err) {
        var result;
        result = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
        output.writeMessageBegin("updateBalance", Thrift.MessageType.EXCEPTION, seqid);
        result.write(output);
        output.writeMessageEnd();
        output.flush();
      });
  } else {
    this._handler.updateBalance(args.accountNumber, args.amount, function (err, result) {
      var result_obj;
      if ((err === null || typeof err === 'undefined')) {
        result_obj = new AccountInformationDB_updateBalance_result((err !== null || typeof err === 'undefined') ? err : {success: result});
        output.writeMessageBegin("updateBalance", Thrift.MessageType.REPLY, seqid);
      } else {
        result_obj = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
        output.writeMessageBegin("updateBalance", Thrift.MessageType.EXCEPTION, seqid);
      }
      result_obj.write(output);
      output.writeMessageEnd();
      output.flush();
    });
  }
};
AccountInformationDBProcessor.prototype.process_addAccount = function(seqid, input, output) {
  var args = new AccountInformationDB_addAccount_args();
  args.read(input);
  input.readMessageEnd();
  if (this._handler.addAccount.length === 1) {
    Q.fcall(this._handler.addAccount, args.accountNumber)
      .then(function(result) {
        var result_obj = new AccountInformationDB_addAccount_result({success: result});
        output.writeMessageBegin("addAccount", Thrift.MessageType.REPLY, seqid);
        result_obj.write(output);
        output.writeMessageEnd();
        output.flush();
      }, function (err) {
        var result;
        result = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
        output.writeMessageBegin("addAccount", Thrift.MessageType.EXCEPTION, seqid);
        result.write(output);
        output.writeMessageEnd();
        output.flush();
      });
  } else {
    this._handler.addAccount(args.accountNumber, function (err, result) {
      var result_obj;
      if ((err === null || typeof err === 'undefined')) {
        result_obj = new AccountInformationDB_addAccount_result((err !== null || typeof err === 'undefined') ? err : {success: result});
        output.writeMessageBegin("addAccount", Thrift.MessageType.REPLY, seqid);
      } else {
        result_obj = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
        output.writeMessageBegin("addAccount", Thrift.MessageType.EXCEPTION, seqid);
      }
      result_obj.write(output);
      output.writeMessageEnd();
      output.flush();
    });
  }
};