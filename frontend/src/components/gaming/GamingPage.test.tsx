import React from 'react';
import { shallow } from 'enzyme';
import GamingPage from './GamingPage';

// TODO: more tests!!
describe('Footer', () => {
    it('renders without crashing', () => {
        shallow(<GamingPage />);
    });
});
