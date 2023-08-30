import React from 'react';
import AppNavigator from './AppNavigator';
import { FitnessContext } from './Context';

export default function App() {
  return (
    <FitnessContext>
    <AppNavigator />
    </FitnessContext>
  );
}
