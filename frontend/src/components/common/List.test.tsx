import React from 'react';
import { shallow } from 'enzyme';
import List from './List';
import { IPage } from '../../interfaces/IPage';

const page: IPage = {
    snippet: 'Test',
    link: 'TestLink',
};

// TODO: more tests!!
describe('Footer', () => {
    it('renders without crashing', () => {
        shallow(<List title="Test" items={[page, page]} />);
    });
});
