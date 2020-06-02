import {createStore} from 'redux';
import main_reducer from '../reducer/main_reducer'

const store = createStore(
    main_reducer
);

export default store;