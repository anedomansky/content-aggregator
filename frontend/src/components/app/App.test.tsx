import React from 'react';
import { shallow } from 'enzyme';
import App from './App';

// TODO: more tests!!
describe('App', () => {
    it('renders without crashing', () => {
        shallow(<App />);
    });
});
