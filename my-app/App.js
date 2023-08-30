import React from 'react';
import AppNavigator from './AppNavigator';
import { FitnessContext } from './Context';
import FitnessPlansScreen from './components/FitnessPlansScreen';

export default function App() {
  return (
    <FitnessContext>
      <FitnessPlansScreen/>
    <AppNavigator />
    </FitnessContext>
  );
}
