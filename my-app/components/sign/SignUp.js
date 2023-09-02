import axios from 'axios';
import React, { useState } from 'react';
import { View, TextInput, Button, Text, Picker,Alert } from 'react-native';

const SignUp = () => {
  
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [username, setUsername] = useState('');
  const [isTrainer, setIsTrainer] = useState(false); // Default to false

  const handleUsernameChange = (text) => {
    setUsername(text);
  };

  const handleEmailChange = (text) => {
    setEmail(text);
  };

  const handlePasswordChange = (text) => {
    setPassword(text);
  };

  const handleIsTrainerChange = (value) => {
    setIsTrainer(value);
  };

  const validateForm = () => {
    if ( !email || !password || !name || !isTrainer || !username ) {
      Alert.alert('Validation Error', 'All fields are required');
      return false;
    }
    return true;
  };
  const handleSubmit = () => {
    if (!validateForm()) {
      return; // Stop the submission if validation fails
    }
    // Prepare the data to send to your backend or perform actions here
    const formData = {
      email:email,
      password:password,
      username:username,
      is_trainer:isTrainer,
    };

    // You can now send formData to your backend API or perform any other actions.
    console.log('Form data:', formData);
    axios.post('http://127.0.0.1:8000/api/signup/',formData)
    .then(res=>{
      console.log(res.data)
      Alert.alert('Message', res.data.msg);
    })
    .catch(err=>{
      console.log(err.message)
      Alert.alert('Error', 'Registration failed');
    })

    // Reset the form fields after submission (if needed)
   
    setEmail('');
    setPassword('');
    setUsername('');
    setIsTrainer(false);
  };

  return (
    <View>
      <TextInput
        placeholder="Email"
        value={email}
        onChangeText={handleEmailChange}
      />
      <TextInput
        placeholder="Unique UserName"
        value={username}
        onChangeText={handleUsernameChange}
      />
      <TextInput
        placeholder="Password"
        value={password}
        onChangeText={handlePasswordChange}
        secureTextEntry={true} // Mask the password input
      />
      <Text>Are You Trainer:</Text>
      <Picker
        selectedValue={isTrainer}
        onValueChange={handleIsTrainerChange}
      >
        <Picker.Item label="Trainer" value={true} />
        <Picker.Item label="User" value={false} />
      </Picker>

      <Button title="Submit" onPress={handleSubmit} />
    </View>
  );
};

export default SignUp;
