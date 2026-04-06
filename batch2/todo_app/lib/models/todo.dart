// ignore_for_file: public_member_api_docs, sort_constructors_first
import 'dart:convert';

class Todo {
  final int id;
  final String task;
  Todo({required this.id, required this.task});

  Todo copyWith({int? id, String? task}) {
    return Todo(id: id ?? this.id, task: task ?? this.task);
  }

  Map<String, dynamic> toMap() {
    return <String, dynamic>{'id': id, 'task': task};
  }

  factory Todo.fromMap(Map<String, dynamic> map) {
    return Todo(id: map['id'] as int, task: map['task'] as String);
  }

  String toJson() => json.encode(toMap());

  factory Todo.fromJson(String source) =>
      Todo.fromMap(json.decode(source) as Map<String, dynamic>);

  @override
  String toString() => 'Todo(id: $id, task: $task)';

  @override
  bool operator ==(covariant Todo other) {
    if (identical(this, other)) return true;

    return other.id == id && other.task == task;
  }

  @override
  int get hashCode => id.hashCode ^ task.hashCode;
}
