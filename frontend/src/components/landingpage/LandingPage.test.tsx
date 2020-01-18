import React from 'react';
import { shallow } from 'enzyme';
import LandingPage from './LandingPage';

// TODO: more tests!!
describe('Footer', () => {
    it('renders without crashing', () => {
        shallow(<LandingPage />);
    });
});
