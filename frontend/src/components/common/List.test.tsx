import React from 'react';
import { shallow } from 'enzyme';
import List from './List';

// TODO: more tests!!
describe('Footer', () => {
    it('renders without crashing', () => {
        shallow(<List title="Test" items={['test1', 'test2']} />);
    });
});
