import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:todo_app/models/todo.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  List<Todo> _todos = [];
  final TextEditingController _controller = TextEditingController();

  //fetching all todo data from the database
  Future<void> _fetchTodos() async {
    final url = Uri.parse('http://localhost:8000/api/list/');
    try {
      final response = await http.get(url);
      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        setState(() {
          _todos = data
              .map<Todo>((e) => Todo.fromMap(e as Map<String, dynamic>))
              .toList();
        });
      }
    } catch (e) {
      print('Error fetching todos: $e');
    }
  }

  @override
  void initState() {
    super.initState();
    _fetchTodos();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  Future<void> _addTodo() async {
    if (_controller.text.isNotEmpty) {
      try {
        final url = Uri.parse('http://localhost:8000/api/list/');
        final response = await http.post(
          url,
          headers: {'Content-Type': 'application/json'},
          body: jsonEncode({'task': _controller.text}),
        );
        print(response.statusCode);
        if (response.statusCode == 200 || response.statusCode == 201) {
          // Successful addition
          final responseData = jsonDecode(response.body);
          setState(() {
            _todos.add(Todo(id: responseData['id'], task: _controller.text));
            _controller.clear();
          });
        } else {
          // Handle error, maybe show a snackbar
          print('Failed to add todo: ${response.statusCode}');
        }
      } catch (e) {
        print('Error adding todo: $e');
      }
    }
  }

  Future<void> _removeTodo(int id) async {
    try {
      final url = Uri.parse('http://localhost:8000/api/detail/$id/');
      final response = await http.delete(url);
      if (response.statusCode == 200 || response.statusCode == 204) {
        // Successful deletion
        setState(() {
          _todos.removeWhere((todo) => todo.id == id);
        });
      } else {
        // Handle error, maybe show a snackbar
        print('Failed to delete todo: ${response.statusCode}');
      }
    } catch (e) {
      print('Error deleting todo: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Todo List')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _controller,
                    decoration: const InputDecoration(
                      hintText: 'Enter a todo item',
                    ),
                    onSubmitted: (_) => _addTodo(),
                  ),
                ),
                const SizedBox(width: 8),
                ElevatedButton(onPressed: _addTodo, child: const Text('Add')),
              ],
            ),
            const SizedBox(height: 16),
            Expanded(
              child: ListView.builder(
                itemCount: _todos.length,
                itemBuilder: (context, index) {
                  return ListTile(
                    title: Text(_todos[index].task),
                    trailing: IconButton(
                      icon: const Icon(Icons.delete),
                      onPressed: () => _removeTodo(_todos[index].id),
                    ),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
