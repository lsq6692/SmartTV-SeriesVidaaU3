
#ifndef BOOST_MPL_TAG_HPP_INCLUDED
#define BOOST_MPL_TAG_HPP_INCLUDED

// Copyright Aleksey Gurtovoy 2004
//
// Distributed under the Boost Software License, Version 1.0. 
// (See accompanying file LICENSE_1_0.txt or copy at 
// http://www.boost.org/LICENSE_1_0.txt)
//
// See http://www.boost.org/libs/mpl for documentation.

// $Id: tag.hpp 386076 2013-10-16 12:24:31Z heinzeti $
// $Date: 2013-10-16 14:24:31 +0200 (Mi, 16. Okt 2013) $
// $Revision: 386076 $

#include <boost/mpl/eval_if.hpp>
#include <boost/mpl/void.hpp>
#include <boost/mpl/aux_/has_tag.hpp>
#include <boost/mpl/aux_/config/eti.hpp>

namespace boost { namespace mpl {

namespace aux {
template< typename T > struct tag_impl
{
    typedef typename T::tag type;
};
}

template< typename T, typename Default = void_ > struct tag
#if !defined(BOOST_MPL_CFG_MSVC_ETI_BUG)
    : if_< 
          aux::has_tag<T>
        , aux::tag_impl<T>
        , Default
        >::type
{
#else
{
    typedef typename eval_if< 
          aux::has_tag<T>
        , aux::tag_impl<T>
        , Default
        >::type type;

#endif
};

}}

#endif // BOOST_MPL_TAG_HPP_INCLUDED
