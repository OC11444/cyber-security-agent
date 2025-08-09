// src/log_canister/main.mo
import Debug "mo:base/Debug";
import Array "mo:base/Array";

actor {
  var logs: [Text] = [];

  public func log(message: Text) : async Text {
    Debug.print("cyber-security-agent log: " # message);
    logs := Array.append<Text>(logs, [message]);
    return "Logged: " # message;
  };

  public query func get_logs() : async [Text] {
    return logs;
  };
}
