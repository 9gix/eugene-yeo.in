Bootstrap Summary
=================

Reference made based on the official documentation `Bootstrap 3.1 <http://getbootstrap.com/>`_

.. code-block:: css

    .container {
        /*
         * center wrapped content
         * fixed width (phone: auto, tablet: 750px, desktop: 970px or 1170px)
         * not nestable 
         */
    }

    .container-fluid {
        /*
         * full width
         */
    }

    /* grid :
     * must be inside container or container-fluid
     */

   /* <DEVICE>: xs, sm, md, lg
    * xs: phone (<768px), 
    * sm: tablet (>=768px), 
    * md: desktop (>=992px), 
    * lg: desktop (>=1200px)
    */

   /* <N-COLUMNS>: 0..12 */

   .col-<DEVICE>-<N-COLUMNS>{
       /* 
        * column width for phone: auto, tablet: 60px, desktop: 78px or 95px)
        * nestable
        * offsets
        * ordering
        * gutter: 30px (15px+15px)
        * example: 
          .col-md-1 { width: 78px }
          .col-md-2 { width: (78 * 2) px }
          .col-md-12 { width: (78 * 12) px }
        * can be combined between different sizes to serve mobile, tablet & desktop 
          <div class="row">
            <div class="col-xs-4 col-sm-6 col-md-8"></div>
            <div class="col-xs-8 col-sm-6 col-md-4"></div>
          </div>
        * if exceed 12 column, the next column will be stacked.
        .clearfix {
            used when the column are not clear on which to start the a new row.
        }
   }

   .col-<DEVICE>-offset-<N-COLUMNS> {
        /* 
         * Move the column to right by * columns. 
         */
   }

    .row {
        /*
         * group horizontal column
         * also used to nest the column
         */
    }

    .col-<DEVICE>-pull-<N-COLUMNS>, .col-<DEVICE>-push-<N-COLUMNS> {
        /* 
         * Manage the column order by pull and push
         */
    }

Minimalistic navbar

.. code-block:: html

    <div class='navbar navbar-default' role='navigation'>
        <div class='container'>
          <div class='navbar-header'><!-- this class only affect on mobile -->
          </div>
          <div class='navbar-collapse'><!-- this class only affect on mobile -->
          </div>
        </div>
    </div>

