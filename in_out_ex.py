---
 - name: How to read and print a variable in playbook
   hosts: target
   gather_facts: no
   vars_prompt:
    - name: username
      prompt: Enter the username
      private: false
    - name: password
      prompt: Enter the password
      private: true
   tasks:
   - debug:
      msg: "The username is: {{username}} and the password is: {{password}}"
